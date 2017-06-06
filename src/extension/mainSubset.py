"""
This module implements the main for Subset class and test the class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""

from src.extension.Interface import *

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

if __name__ == "__main__":
    Interface.inputOptions()
    tableNames = list(
        six.moves.input("Please enter the table names for the graf creation with spaces between them:\n").split())

    # initGraph
    tables, cursor = Data.getTablesForGraphCreation(tableNames)  # Get tables from SQLite database
    initGraph = Graph.initGraph(tables, cursor)  # Initialize a graph

    optionGraph = int(
        six.moves.input("Please enter the option of graph you want to create:\n [1] = plain\n [2] = plain "
                        "with threshold\n [3] = linear\n [4] = exponential\n"))

    rows = Data.selectDataTables(tables)  # Select rows from SQLite tables
    graph, graphName = Interface.graphOptions(optionGraph, initGraph, rows)  # Create a type of graph
    print("Subsets of graph:")
    for subset in Subset.powerSetGenerator(graph.nodes()):  # All subsets from a graph
        print(subset)
