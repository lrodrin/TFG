"""
This module implements a main for the Graph class and test the class with a simple graphs

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
from src.final.Interface import *
# from src.final.simpleGraphs import *

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

if __name__ == '__main__':
    # graph = simpleGraph_1()  # Create a simple graph
    # graphName = "simpleGraph1.dot"
    # Graph.exportGraph(graph, graphName)  # Export graph to DOT format
    # Interface.openGraphviz(graphName)  # Open graph in Graphviz program
    #
    # graph = simpleGraph_2()  # Create a simple graph
    # graphName = "simpleGraph2.dot"
    # Graph.exportGraph(graph, graphName)  # Export graph to DOT format
    # Interface.openGraphviz(graphName)  # Open graph in Graphviz program

    optionData = int(six.moves.input("Please enter the option for the type of file you provide:\n [1] = ARFF\n [2] = "
                                     "TXT\n [3] = DB\n"))

    columnNames, rows, cursor, tableName = Interface.inputFileOptions(optionData)  # Manages the data entry
    initGraph, rows = Graph.initGraph(tableName, cursor)  # Initialize a graph

    optionGraph = int(
        six.moves.input("Please enter the option of graph you want to create:\n [1] = plain\n [2] = plain "
                        "with threshold\n [3] = linear\n [4] = exponential\n"))
    graph, graphName = Interface.graphOptions(optionGraph, initGraph, rows)  # Create a type of graph
    Interface.openGraphviz(graphName)  # Open graph in Graphviz program
