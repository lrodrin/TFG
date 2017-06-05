"""
This module implements the main for Structure class and test the class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""

from src.extension.Interface import *

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

if __name__ == "__main__":
    optionData = int(six.moves.input("Please enter the option for the type of file you provide:\n [1] = ARFF\n [2] = "
                                     "TXT\n [3] = DB\n"))

    columnNames, rows, cursor, tableName = Interface.inputFileOptions(optionData)  # Manages the data entry
    initGraph, rows = Graph.initGraph(tableName, cursor)  # Initialize the graph

    optionStructure = int(
        six.moves.input("Please enter the option of 2-structure you want to create:\n [1] = plain\n [2] = plain "
                        "with threshold\n [3] = linear\n [4] = exponential\n"))
    graph, graphName = Interface.graphOptions(optionStructure, initGraph, rows)  # Create a type of graph
    structureName = Interface.structureOptions(optionStructure, graph, None)  # Create 2-structure from graph
    Interface.openGraphviz(structureName)
