"""
This module implements the main for Structure class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
from src.final.Structure import *
from src.simpleGraphs import *

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

if __name__ == "__main__":
    simpleGraph_1 = simpleGraph_1()
    Structure.create2Structure(simpleGraph_1, simpleGraph_1.nodes(), 'Structure.dot')

    simpleGraph_2 = simpleGraph_2()
    Structure.create2Structure(simpleGraph_2, simpleGraph_2.nodes(), 'Structure2.dot')

    # optionData = int(six.moves.input("Please enter the option for the type of file you provide:\n [1] = ARFF\n [2] = "
    #                                  "TXT\n [3] = DB\n"))
    #
    # columnNames, rows, cursor, tableName = Data.inputFileOptions(optionData)  # Manages the data entry
    # initGraph, rows = Graph.initGraph(tableName, cursor)  # Initialize the graph
    #
    # optionGraph = int(
    #     six.moves.input("Please enter the option of graph you want to create:\n [1] = plain\n [2] = plain "
    #                     "with threshold\n [3] = linear\n [4] = exponential\n"))
    # Graph.graphOptions(optionGraph, initGraph, rows)  # Create a type of graph
    #
    # option = int( six.moves.input("Please enter the option of 2-structure you want to create:\n [1] = plain\n [2] =
    #  linear\n [3] " "= exponential\n")) if option == 1: optionPlain = int( six.moves.input("Please enter the option
    #  of plain initGraph you want to create:\n [1] = plain\n [2] = " "plain with threshold\n")) if optionPlain == 1:
    #  filename = "plain 2-structure.dot" plainGraph = Graph.createPlainGraph(graph, rows)  # Create a plain
    # initGraph elif optionPlain == 2: filename = "plain 2-structure with threshold.dot" threshold = int(
    # six.moves.input("Please enter the k constant for the threshold:\n")) plainGraph =
    # Graph.createPlainGraphWithThreshold(graph, rows, threshold)  # Create a plain initGraph with threshold
    #
    #     Structure.create2Structure(plainGraph, plainGraph.nodes(), filename)  # Create a plain 2-structure
    #
    # elif option == 2:
    #     linearGraph = Graph.createLinearGraph(graph, rows)  # Create a linear initGraph
    #     Structure.linear2structure(linearGraph, linearGraph.nodes(),
    #                                "linear 2-structure.dot")  # Create a linear 2-structure
    # elif option == 3:
    #     exponentialGraph = Graph.createExponentialGraph(graph, rows)  # Create an exponential simpleGraph
    #     Structure.exponential2structure(exponentialGraph,
    #                                     exponentialGraph.nodes(),
    #                                     "exponential 2-structure.dot")  # Create an exponential 2-structure
