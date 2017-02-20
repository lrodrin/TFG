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
except sqlite3.Error as e:  # TODO de FILES!!!!
    print("Error:", e)

lines = file.readlines()  # Keep all lines from data file into lines
header = lines[0]  # Extract the header from data file
colNames = ""
colCounter = 0  # Counter to count the number of columns from data file
for word in header.split(" "):  # For each word from header, keep a column in colNames
    colNames += word + ", "  # Adding a column
    colCounter += 1  # Increase the number of columns

file.close()

try:
    tableName = str(input("Please enter a name for the database table: "))
    query = "CREATE TABLE %s (%s);" % (str(tableName), str(colNames[0:-2]))  # Create the table if not exists
    print(query)
    # cur.execute(query)
except sqlite3.Error as e:
    print("Error:", e)

l = ""
for i in range(1, len(lines)):
    for j in lines[i].split(" "):
        # l += j.split(":")[1] + ", "
        l += "'%s'," % j.split(":")[1]
    # print(l[0:-2])
    query = 'INSERT INTO {0} ({1}) VALUES ({2});'.format(str(tableName), str(colNames[0:-2]), str(l[0:-1]))
    # cur.execute('INSERT OR IGNORE INTO test ( outlook, temperature, humidity, windy, play) VALUES (?, ?, ?, ? , ?)',
    #             (d[0].split(':')[1], d[1].split(':')[1], d[2].split(':')[1], d[3].split(':')[1], d[4].split(':')[1]))
    print(query)
    cur.execute(query)
    l = ""
    connection.commit()

cur.close()
connection.close()
# TODO fusionar amb gaifman
