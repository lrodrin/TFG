"""
This module implements the main for Data class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
import os

import src.final.Data as d

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

if __name__ == "__main__":
    pathBD = str(input("Please enter a path from database file: "))
    # C:/Users/Laura/PycharmProjects/TFG/src/SQL/BD.db
    connection = d.Data.connection(pathBD)   # Connection to database
    cursor = connection.cursor()

    pathFile = str(input("Please enter a path from data file: "))
    # C:/Users/Laura/PycharmProjects/TFG/src/SQL/meteo.txt
    file = d.Data.open_file(pathFile)   # Open data file

    colNames, lines = d.Data.get_data_from_file(file)  # Keep column names and lines from data file

    tableName = str(input("Please enter a name for the database table: "))
    d.Data.create_table(cursor, tableName, colNames)    # Create table
    d.Data.insert(tableName, colNames, lines, cursor, connection)   # Insert data to table
    ############################## GAIFMAN METHODS ##################################
    # os.startfile('Estructura.dot')  # Launch Graphviz program that is associated with this file
    d.Data.close(file, cursor, connection)