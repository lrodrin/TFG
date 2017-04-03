"""
This module implements the main for Interface class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""

from src.final.Interface import *
from src.final.simpleGraphs import *

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

if __name__ == '__main__':
    # Simple graphs
    simpleGraph_1 = simpleGraph_1()  # Create a simple graph
    Structure.create2Structure(simpleGraph_1, simpleGraph_1.nodes(), 'Structure.dot')  # Create a 2-structure

    simpleGraph_2 = simpleGraph_2()  # Create a simple graph
    Structure.create2Structure(simpleGraph_2, simpleGraph_2.nodes(), 'Structure2.dot')  # Create a 2-structure

    optionData = int(six.moves.input("Please enter the option for the type of file you provide:\n [1] = ARFF\n [2] = "
                                     "TXT\n [3] = DB\n"))
    columnNames, rows, cursor, tableName = Interface.inputFileOptions(optionData)  # Manages the data entry
    initGraph, rows = Graph.initGraph(tableName, cursor)  # Initialize the graph

    optionStructure = int(
        six.moves.input("Please enter the option of 2-structure you want to create:\n [1] = plain\n [2] = plain "
                        "with threshold\n [3] = linear\n [4] = exponential\n"))
    graph, graphName = Interface.graphOptions(optionStructure, initGraph, rows)  # Create a type of graph
    structureName = Interface.structureOptions(optionStructure, graph)  # Create 2-structure from a graph
    Interface.openGraphviz(graphName)  # Open graph in Graphviz program
    Interface.openGraphviz(structureName)  # Open 2-structure in Graphviz program
