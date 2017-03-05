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
    # C:/Users/Laura/PycharmProjects/TFG/src/SQL/BD.db  WINDOWS
    # /Users/laura/PycharmProjects/TFG/src/SQL/BD.db    OS X
    connection = Data.connection(fileDB)  # Connection to SQLite database
    cursor = connection.cursor()

    dataFile = str(input("Please enter data file:\n"))
    # TODO ARFF format
    # C:/Users/Laura/PycharmProjects/TFG/src/SQL/meteo.txt  WINDOWS
    # /Users/laura/PycharmProjects/TFG/src/SQL/meteo.txt    OS X
    file = Data.openFile(dataFile)  # Open data file
    columnNames, lines = Data.getDataFile(file)  # Get column names and lines from file

    tableName = str(input("Table name: \n"))
    Data.createTable(cursor, tableName, columnNames)  # Create table tableName
    Data.insert(tableName, columnNames, lines, cursor, connection)  # Insert data to tableName
    columnNames, rows = Data.select(tableName, cursor)  # Select column names and rows from tableName
