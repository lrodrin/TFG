"""
This module implements the main for Data class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
import six

from src.final.Data import *

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

if __name__ == "__main__":
    fileDB = str(six.moves.input("Please enter the name from SQLite file:\n"))
    connection, cursor = Data.connection(fileDB)  # Connection to SQLite database
    #
    # dataFile = str(six.moves.input("Please enter the name from txt file:\n"))
    # file = Data.openFile(dataFile)  # Open data file
    # columnNames, lines = Data.getDataFile(file)  # Get column names and lines from file
    #
    tableName = str(six.moves.input("Please enter the table name: \n"))
    # Data.createTable(cursor, tableName, columnNames)  # Create table tableName
    # Data.insert(tableName, columnNames, lines, cursor, connection)  # Insert data values to tableName
    columnNames, rows = Data.select(tableName, cursor)  # Select data from tableName
    print(columnNames)
    print(rows)

    tables = Data.getTablesNames(cursor)  # Get tables name from SQLite database
    print("List of tables:\n", tables)
