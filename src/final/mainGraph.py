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
    fileOption = int(six.moves.input("Please enter the option for the type of file you provide:\n [1] = ARFF\n [2] = "
                                     "TXT\n [3] = DB\n"))
    if fileOption == 1:
        fileARFF = str(six.moves.input("Please enter the name from ARFF file:\n")) + ".arff"
        # connection, cursor = Data.connection(file[0:-5] + ".db")  # Connection to SQLite database
        connection, cursor = Data.connection("DB")  # Connection to SQLite database
        file = Data.openFile(fileARFF)  # Open data file
        columnNames, lines = Data.getDataFile(file, "ARFF")  # Get column names and lines from data file
        tableName = Data.getNameForTableNameFromARFF(lines)  # Get table name from data file
        Data.createTable(cursor, tableName, columnNames)  # Create table tableName
        Data.insertARFF(tableName, columnNames, lines, cursor, connection)  # Insert data values to tableName
        columnNames, rows = Data.select(tableName, cursor)  # Select data from tableName

    elif fileOption == 2:
        fileTXT = str(six.moves.input("Please enter the name from TXT file:\n")) + ".txt"
        # connection, cursor = Data.connection(file[0:-4] + ".db")  # Connection to SQLite database
        connection, cursor = Data.connection("DB")  # Connection to SQLite database
        file = Data.openFile(fileTXT)  # Open data file
        columnNames, lines = Data.getDataFile(file, "TXT")  # Get column names and lines from file
        tableName = str(
            six.moves.input("Please enter the table name which to create the new SQLite table from file: \n"))
        Data.createTable(cursor, tableName, columnNames)  # Create table tableName
        Data.insertTXT(tableName, columnNames, lines, cursor, connection)  # Insert data values to tableName
        columnNames, rows = Data.select(tableName, cursor)  # Select data from tableName

    elif fileOption == 3:
        file = str(six.moves.input("Please enter the name from SQLite file:\n")) + ".db"
        connection, cursor = Data.connection("DB")  # Connection to SQLite database
        tableName = str(
            six.moves.input("Please enter the table name which to select from SQLite database: \n"))
        columnNames, rows = Data.select(tableName, cursor)  # Select data from tableName

    graph, rows = Graph.initializeGraph(tableName, cursor)  # Initialize the initGraph

    option = int(
        six.moves.input("Please enter the option of initGraph you want to create:\n [1] = plain\n [2] = plain with "
                        "threshold\n [3] = linear\n [4] = exponential\n"))
    if option == 1:
        plainGraph = Graph.createPlainGraph(graph, rows)  # Create a plain initGraph
        Graph.exportGraphDOT(graph, 'plainGraph.dot')  # Export simpleGraph to Graphviz format
        print("Plain initGraph was created")
    elif option == 2:
        threshold = int(six.moves.input("Please enter the k constant for the threshold:\n"))
        plainGraph = Graph.createPlainGraphWithThreshold(graph, rows, threshold)  # Create a plain initGraph with threshold
        Graph.exportGraphDOT(graph, 'plainGraph with threshold.dot')  # Export initGraph to Graphviz format
        print("Plain initGraph with threshold was created")
    elif option == 3:
        linearGraph = Graph.createLinearGraph(graph, rows)  # Create a linear initGraph
        Graph.exportGraphDOT(graph, 'linearGraph.dot')  # Export initGraph to Graphviz format
        print("Linear initGraph was created")
    elif option == 4:
        exponentialGraph = Graph.createExponentialGraph(graph, rows)  # Create an exponential initGraph
        Graph.exportGraphDOT(graph, 'exponentialGraph.dot')  # Export initGraph to Graphviz format
        print("Exponential initGraph was created")
