"""
This module implements the main for Data class and test the class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""

from src.extension.Interface import *

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

if __name__ == "__main__":
    option = int(six.moves.input("Please enter the option for the type of file you provide:\n [1] = ARFF\n [2] = "
                                 "TXT\n [3] = DB\n"))

    columnNames, rows, cursor, tableName = Interface.inputFileOptions(option)  # Manages the data entry

    tableNames = list(six.moves.input("Please enter the table names you provide with spaces between them:\n").split())
    tables, cursor = Data.getTableNamesDB(tableNames)  # Get tables names from SQLite database
    print("SQLite tables:\n", tables)

    rowsList = Data.selectDataTables(tables)    # Select rows from different SQLite tables
    print("Rows from SQLite tables", tables)
    print(rowsList)
