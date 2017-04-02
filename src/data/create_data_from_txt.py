"""
This module creates a table for a SQLite database from TXT file

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
from src.final.Data import *

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

# C:/Users/Laura/PycharmProjects/TFG/src/data/DB.db  WINDOWS
# /Users/laura/PycharmProjects/TFG/src/data/DB.db    OS X
connection, cursor = Data.connectionDB('C:/Users/Laura/PycharmProjects/TFG/src/data/DB')  # Connection to SQLite
# database

fileName = str(input("Please enter the file name you provide:\n"))
file = Data.openFile("C:/Users/Laura/PycharmProjects/TFG/src/data/%s.txt" % fileName)  # Open data file

columnNames, lines = Data.getDataFile(file, "TXT")  # Get data from file
# print(columnNames)
Data.createTable(cursor, fileName, columnNames)  # Create SQLite table
Data.insertDataTXT(fileName, columnNames, lines, cursor, connection)  # Insert data values into SQLite table

file.close()
cursor.close()
connection.close()
