"""
This module implements the main for the more frequent Clan class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
import six

from src.final.Clan import *
from src.final.Graph import *

# from src.simpleGraphs import *

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

if __name__ == "__main__":
    # graph = simpleGraph_1()  # Create a simple graph
    # print("Simple graph\n")
    # Clan.printResults(graph)
    #
    # graph = simpleGraph_2()  # Create a simple graph
    # print("\nSimple graph\n")
    # Clan.printResults(graph)

    optionData = int(six.moves.input("Please enter the option for the type of file you provide:\n [1] = ARFF\n [2] = "
                                     "TXT\n [3] = DB\n"))

    columnNames, rows, cursor, tableName = Interface.inputFileOptions(optionData)  # Manages the data entry
    initGraph, rows = Graph.initGraph(tableName, cursor)  # Initialize the graph

    optionGraph = int(
        six.moves.input("Please enter the option of graph you want to create:\n [1] = plain\n [2] = plain "
                        "with threshold\n [3] = linear\n [4] = exponential\n"))
    graph = Interface.graphOptions(optionGraph, initGraph, rows)  # Create a type of graph

    filename = str(six.moves.input("Please enter the file name you provide:\n"))
    probability = float(six.moves.input("Please enter the probability for the more frequent subsets creation:\n"))
    moreFrequentSubsets = Subset.moreFrequentSubsets(filename, optionData, probability)  # The more frequents subsets
    #  from filename
    print(moreFrequentSubsets)

    plainGraph = Graph.createPlainGraph(initGraph, rows)  # Create plain graph
    print("\nPlain graph\n")
    Clan.printFrequentResults(plainGraph)

    plainGraphWithThreshold = Graph.createPlainGraphWithThreshold(initGraph, rows, 3)  # Create a plain graph with
    # threshold
    print("\nPlain graph with threshold\n")
    Clan.printFrequentResults(plainGraphWithThreshold)

    linearGraph = Graph.createLinearGraph(initGraph, rows)  # Create linear graph
    print("\nLinear graph\n")
    Clan.printFrequentResults(linearGraph)

    exponentialGraph = Graph.createExponentialGraph(initGraph, rows)  # Create exponential graph
    print("\nExponential graph\n")
    Clan.printFrequentResults(exponentialGraph)
