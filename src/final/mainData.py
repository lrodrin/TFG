"""
This module implements the main for Data class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
from src.final.Data import *

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

if __name__ == "__main__":
    fileDB = str(input("Please enter a database SQLite file:\n"))
    # C:/Users/Laura/PycharmProjects/TFG/src/final/DB.db  WINDOWS
    # /Users/laura/PycharmProjects/TFG/src/final/DB.db    OS X
    connection, cursor = Data.connection(fileDB)  # Connection to SQLite database

    dataFile = str(input("Please enter data file:\n"))
    # # C:/Users/Laura/PycharmProjects/TFG/src/final/weather.txt  WINDOWS
    # # /Users/laura/PycharmProjects/TFG/src/final/weather.txt    OS X
    file = Data.openFile(dataFile)  # Open data file
    columnNames, lines = Data.getDataFile(file)  # Get column names and lines from file

    tableName = str(input("Table name: \n"))
    Data.createTable(cursor, tableName, columnNames)  # Create table tableName
    Data.insert(tableName, columnNames, lines, cursor, connection)  # Insert data to tableName

    tables = Data.geTablesNames(cursor)
    print(tables)