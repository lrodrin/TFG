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
    fileOption = int(input("Please enter the option for the file you provide:\n [1] = .arff\n [2] = .db\n"))
    if fileOption == 1:
        file = str(input("Please enter the name from arff file:\n"))
        connection, cursor = Data.connection(file[0:-5] + ".db")  # Connection to SQLite database
        file = Data.openFile(file)  # Open data file
        columnNames, lines = Data.getDataARFFile(file)  # Get column names and lines from data file
        tableName = Data.getTableNameFromARFFFile(lines)    # Get table name from data fila
        Data.createTableARFF(cursor, tableName, columnNames)  # Create table tableName
        Data.insertARFF(tableName, columnNames, lines, cursor, connection)  # Insert data values to tableName

        columnNames, rows = Data.select(tableName, cursor)  # Select data from tableName
        print(columnNames)
        print(rows)

    elif fileOption == 2:
        file = str(input("Please enter the name from SQLite file:\n"))
        connection, cursor = Data.connection(file)  # Connection to SQLite database
        tableName = str(input("Please enter the table name: \n"))
        columnNames, rows = Data.select(tableName, cursor)  # Select data from tableName
        print(columnNames)
        print(rows)

    tables = Data.getTablesNames(cursor)  # Get tables name from SQLite database
    print("List of tables:\n", tables)
