"""
This module implements a table for a database from arff file

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
file = Data.openFile('C:/Users/Laura/PycharmProjects/TFG/src/data/weather.arff')  # Open data file

# get data
lines = file.readlines()
columnNames = str()
for line in lines:
    if line.startswith("@attribute"):
        columnNames += line.split(" ")[1] + ", "

# create table
query = "CREATE TABLE %s (%s);" % (str('test'), str(columnNames[0:-2]))
print(query)
cursor.execute(query)

# insert values into table
values = str()
for line in lines:
    if not line.startswith("@") and not line.startswith("\n"):
        for word in line.split(","):
            word = "'{0}'".format(word.replace('\n', ''))
            values += word + ','
        query = 'INSERT INTO {0} ({1}) VALUES ({2});'.format(str('test'), str(columnNames[0:-2]),
                                                             str(values[0:-1]).replace('\n', ''))
        # print(query)
        cursor.execute(query)
        connection.commit()
        values = str()
Data.close(file, cursor, connection)
