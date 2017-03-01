"""
This module implements the main for Data class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
import src.final.Data as d
import src.final.Estructura as e

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

if __name__ == "__main__":
    pathBD = str(input("Please enter a path from database file: "))
    # C:/Users/Laura/PycharmProjects/TFG/src/SQL/BD.db
    # /Users/laura/PycharmProjects/TFG/src/SQL/BD.db
    connection = d.Data.connection(pathBD)  # Connection to database
    cursor = connection.cursor()

    pathFile = str(input("Please enter a path from data file: "))
    # C:/Users/Laura/PycharmProjects/TFG/src/SQL/meteo.txt
    # /Users/laura/PycharmProjects/TFG/src/SQL/meteo.txt
    file = d.Data.open_file(pathFile)  # Open data file

    colNames, lines = d.Data.get_data_from_file(file)  # Keep column names and lines from data file

    tableName = str(input("Please enter a name for the database table: "))

    d.Data.create_table(cursor, tableName, colNames)  # Create tableName
    d.Data.insert(tableName, colNames, lines, cursor, connection)  # Insert data to tableName
    d.Data.select(tableName, cursor)    # Select data from tableName

    print("Open Graphviz program...")
    e.Estructura.openGraphviz('/Applications/Graphviz.app', 'Estructura.dot')  # OS X
    # e.Estructura.openGraphviz('', 'Estructura.dot')  # WINDOWS
    d.Data.close(file, cursor, connection)
