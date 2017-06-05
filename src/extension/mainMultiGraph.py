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
    tableNames = list(six.moves.input("Please enter the table names you provide:\n"))
    # initMultiGraph from different SQLite tables
    tables, cursor = Data.getTableNamesDB(tableNames)
    initGraph = Graph.initMultiGraph(tables, cursor)  # Initialize a graph
    Graph.exportGraph(initGraph, "initMultiGraph.dot")
    Interface.openGraphviz("initMultiGraph.dot")

    # optionGraph = int(
    #     six.moves.input("Please enter the option of graph you want to create:\n [1] = plain\n [2] = plain "
    #                     "with threshold\n [3] = linear\n [4] = exponential\n"))
    # graph, graphName = Interface.graphOptions(optionGraph, initGraph, rows)  # Create a type of graph
    #
    # if nx.number_of_nodes(graph) <= 15:
    #     Interface.openGraphviz(graphName)  # Open graph in Graphviz program
