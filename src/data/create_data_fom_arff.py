"""
This module creates a table for a SQLite database from arff

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
from src.final.Data import *

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

# fileDB = str(input("Please enter a database SQLite file:\n"))
# C:/Users/Laura/PycharmProjects/TFG/src/data/BD.db  WINDOWS
# /Users/laura/PycharmProjects/TFG/src/data/BD.db    OS X
connection, cursor = Data.connection('C:/Users/Laura/PycharmProjects/TFG/src/data/BD.db')  # Connection to SQLite
# database

# dataFile = str(input("Please enter data file:\n"))
# C:/Users/Laura/PycharmProjects/TFG/src/data/weather.arff  WINDOWS
# /Users/laura/PycharmProjects/TFG/src/data/weather.arff    OS X
file = Data.openFile('C:/Users/Laura/PycharmProjects/TFG/src/data/contact-lenses.arff')  # Open data file

# get data
lines = file.readlines()
columnNames = str()
for line in lines:
    if line.startswith("@attribute") or line.startswith("@ATTRIBUTE"):
        name = line.split(" ")[1]
        columnNames += name + ", "

print(columnNames)
# create table
tableName = str(input("Table name:\n"))
query = 'CREATE TABLE {0} ({1});'.format(str(tableName), str(columnNames[0:-2]))
print(query)
cursor.execute(query)

# insert values into table
values = str()
for line in lines:
    if not line.startswith("@") and not line.startswith("\n") and not line.startswith("%"):
        for word in line.split(","):
            word = "'{0}'".format(word.replace('\n', ''))
            values += word + ','
        try:
            query = 'INSERT INTO {0} ({1}) VALUES ({2})'.format(str(tableName), str(columnNames[0:-2]),
                                                                str(values[0:-1]).replace('\n', ''))
            cursor.execute(query)
            connection.commit()
            print("Row %s inserted" % query)
            values = str()
        except sqlite3.Error as e:
            print("Error insert:", e)
Data.close(file, cursor, connection)
