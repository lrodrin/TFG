"""
This module implements a main for the Graph class and test the class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""

from src.extension.Interface import *

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

if __name__ == '__main__':
    optionData = int(six.moves.input("Please enter the option for the type of file you provide:\n [1] = ARFF\n [2] = "
                                     "TXT\n [3] = DB\n"))

    columnNames, rows, cursor, tableName = Interface.inputFileOptions(optionData)  # Manages the data entry
    # initGraph
    initGraph, rows = Graph.initGraph(tableName, cursor)  # Initialize a graph
    Graph.exportGraph(initGraph, "initGraph.dot")
    Interface.openGraphviz("initGraph.dot")

    # initMultiGraph from different SQLite tables
    tableNames = Data.getTableNamesDB(cursor)
    initGraph = Graph.initMultiGraph(tableNames, cursor)  # Initialize a graph
    Graph.exportGraph(initGraph, "initGraph2.dot")
    Interface.openGraphviz("initGraph2.dot")

    # optionGraph = int(
    #     six.moves.input("Please enter the option of graph you want to create:\n [1] = plain\n [2] = plain "
    #                     "with threshold\n [3] = linear\n [4] = exponential\n"))
    # graph, graphName = Interface.graphOptions(optionGraph, initGraph, rows)  # Create a type of graph
    #
    # if nx.number_of_nodes(graph) <= 15:
    #     Interface.openGraphviz(graphName)  # Open graph in Graphviz program
