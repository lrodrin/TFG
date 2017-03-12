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
        file = str(input("Please enter the name from ARFF data file:\n"))
        name = file[0:-5]
        connection, cursor = Data.connection(name + ".db")  # Connection to SQLite database
        file = Data.openFile(file)  # Open data file
        columnNames, lines = Data.getDataARFFile(file)  # Get column names and lines from file
        Data.createTableARFF(cursor, name, columnNames)  # Create table tableName
        Data.insertARFF(name, columnNames, lines, cursor, connection)  # Insert data to tableName
    elif fileOption == 2:
        file = str(input("Please enter the name from DB SQLite file:\n"))
        connection, cursor = Data.connection(file)  # Connection to SQLite database

    tableName = str(input("Table name: \n"))
    Data.select(tableName,cursor)

