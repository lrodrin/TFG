"""
This module implements a Gaifman graph from database and create a 2-structure of this graph

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
from src.final.Graph import *

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

if __name__ == '__main__':
    fileOption = int(input("Please enter the option for the file you provide:\n [1] = .arff\n [2] = .db\n"))
    if fileOption == 1:
        file = str(input("Please enter the name from ARFF data file:\n"))
        # connection, cursor = Data.connection(file[0:-5] + ".db")  # Connection to SQLite database
        connection, cursor = Data.connection("DB" + ".db")  # Connection to SQLite database
        # file = Data.openFile(file)  # Open data file
        # columnNames, lines = Data.getDataARFFile(file)  # Get column names and lines from file
        # tableName = Data.getTableNameFromARFFFile(lines)
        # Data.createTableARFF(cursor, tableName, columnNames)  # Create table tableName
        # Data.insertARFF(tableName, columnNames, lines, cursor, connection)  # Insert data to tableName
    elif fileOption == 2:
        file = str(input("Please enter the name from DB SQLite file:\n"))
        connection, cursor = Data.connection(file)  # Connection to SQLite database

    tableName = str(input("Table name: \n"))
    graph, rows = Graph.initializeGraph(tableName, cursor)

    option = int(input("Please enter the option of graph you want to create:\n [1] = plain\n [2] = linear\n [3] "
                       "= exponential\n [4] = plain with threshold\n"))
    if option == 1:
        plainGraph = Graph.createPlainGraph(graph, rows)
        Graph.exportGraphDOT(graph, 'plainGraph.dot')
    elif option == 2:
        linearGraph = Graph.createLinearGraph(graph, rows)
        Graph.exportGraphDOT(graph, 'linearGraph.dot')
    elif option == 3:
        exponentialGraph = Graph.createExponentialGraph(graph, rows)
        Graph.exportGraphDOT(graph, 'exponentialGraph.dot')
    elif option == 4:
        threshold = int(input("Please enter the k constant for the threshold:\n"))
        plainGraph = Graph.createPlainGraphWithThreshold(graph, rows, threshold)
        Graph.exportGraphDOT(graph, 'plainGraphWithThreshold.dot')
