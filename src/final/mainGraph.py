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
    option = int(six.moves.input("Please enter the option for the type of file you provide:\n [1] = ARFF\n [2] = "
                                 "TXT\n [3] = DB\n"))

    columnNames, rows, cursor = Data.inputFileOptions(option)  # Manages the data entry

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
