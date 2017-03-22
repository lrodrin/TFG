"""
This module implements a Gaifman graph from database and create a 2-structure of this graph

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
from src.final.Graph import *
import six

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

if __name__ == '__main__':
    fileOption = int(six.moves.input("Please enter the option for the file you provide:\n [1] = .arff\n [2] = .db\n"))
    if fileOption == 1:
        file = str(six.moves.input("Please enter the name from arff file:\n"))
        connection, cursor = Data.connection(file[0:-5] + ".db")  # Connection to SQLite database
        file = Data.openFile(file)  # Open data file
        columnNames, lines = Data.getDataARFFile(file)  # Get column names and lines from data file
        tableName = Data.getTableNameFromARFFFile(lines)  # Get table name from data file
        Data.createTableARFF(cursor, tableName, columnNames)  # Create table tableName
        Data.insertARFF(tableName, columnNames, lines, cursor, connection)  # Insert data values to tableName

    elif fileOption == 2:
        file = str(six.moves.input("Please enter the name from SQLite file:\n"))
        connection, cursor = Data.connection(file)  # Connection to SQLite database

    tableName = str(six.moves.input("Please enter the table name: \n"))
    graph, rows = Graph.initializeGraph(tableName, cursor)  # Initialize the graph

    option = int(
        six.moves.input("Please enter the option of graph you want to create:\n [1] = plain\n [2] = plain with "
                        "threshold\n [3] = linear\n [4] = exponential\n"))
    if option == 1:
        plainGraph = Graph.createPlainGraph(graph, rows)  # Create a plain graph
        Graph.exportGraphDOT(graph, 'plainGraph.dot')  # Export graph to Graphviz format
        print("Plain graph was created")
    elif option == 2:
        threshold = int(six.moves.input("Please enter the k constant for the threshold:\n"))
        plainGraph = Graph.createPlainGraphWithThreshold(graph, rows, threshold)  # Create a plain graph with threshold
        Graph.exportGraphDOT(graph, 'plainGraph with threshold.dot')  # Export graph to Graphviz format
        print("Plain graph with threshold was created")
    elif option == 3:
        linearGraph = Graph.createLinearGraph(graph, rows)  # Create a linear graph
        Graph.exportGraphDOT(graph, 'linearGraph.dot')  # Export graph to Graphviz format
        print("Linear graph was created")
    elif option == 4:
        exponentialGraph = Graph.createExponentialGraph(graph, rows)  # Create an exponential graph
        Graph.exportGraphDOT(graph, 'exponentialGraph.dot')  # Export graph to Graphviz format
        print("Exponential graph was created")
