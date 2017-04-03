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

    file = str(six.moves.input("Please enter the name from SQLite file:\n"))
    connection, cursor = Data.connectionDB(file)  # Connection to SQLite database
    tableName = str(six.moves.input("Please enter the table name which to create graph: \n"))
    initGraph, rows = Graph.initGraph(tableName, cursor)  # Initialize the initGraph

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
