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
    Interface.inputOptions()
    tableNames = list(
        six.moves.input("Please enter the table names for the graf creation with spaces between them:\n").split())
    tables, cursor = Data.getTablesForGraphCreation(tableNames)  # Get tables from SQLite database
    print("SQLite tables\n", tables)

    rowsList = Data.selectDataTables(tables)  # Select rows from SQLite tables
    print("Rows from SQLite tables", tables)
    print(rowsList)
