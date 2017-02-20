"""
This module implements a table for a database

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
import sqlite3

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

# global variables
connection = ""
file = ""
query = ""
tableName = ""

try:
    connection = sqlite3.connect('C:/Users/Laura/PycharmProjects/TFG/src/SQL/BD.db')  # Connection to database
    # pathBD = str(input("Please enter a path from database file: "))
    # connection = sqlite3.connect(pathBD)
except sqlite3.Error as e:
    print("Error:", e)

cur = connection.cursor()

try:
    file = open('C:/Users/Laura/PycharmProjects/TFG/src/SQL/meteo.txt', 'r')  # Open data file
    # pathFile = str(input("Please enter a path from data file: "))
    # file = open(pathFile, 'r')
except IOError as e:
    print("Error:", e)

lines = file.readlines()  # Keep all lines from data file into lines
header = lines[0]  # Extract the header from lines
colNames = ""
for word in header.split(" "):  # For each word from header
    colNames += word + ", "  # Adding a column into colNames

try:
    tableName = str(input("Please enter a name for the database table: "))
    query = "CREATE TABLE %s (%s);" % (str(tableName), str(colNames[0:-2]))  # Create a table
    # print(query)
    cur.execute(query)
    print("Created table %s..." % tableName)
except sqlite3.Error as e:
    print("Error:", e)

values = ""
for i in range(1, len(lines)):  # For each row from data file
    for col in lines[i].split(" "):   # For each column in lines[i]
        values += "'%s'," % col.split(":")[1]   # Extract and save the value
    try:
        query = 'INSERT INTO {0} ({1}) VALUES ({2});'.format(str(tableName), str(colNames[0:-2]), str(values[0:-1]))
        # Insert values to table
        # print(query)
        cur.execute(query)
        connection.commit()
        print("Inserted row number %d" % i)
    except sqlite3.Error as e:
        print("Error:", e)
    values = ""

file.close()
cur.close()
connection.close()
