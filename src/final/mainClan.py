"""
This module implements the main for Clan class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
import six

from src.final.Clan import *
from src.final.Graph import *
from src.simpleGraphs import *

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'


def printResults(graph):
    """
    Print the results of the main execution:
        - A list of clans
        - A list of trivial clans
        - A list of primal clans
        - A dictionary of primal clans

    :param graph: Networkx's graph
    :type graph: nx.Graph
    """
    clansList = Clan.clans(graph, graph.nodes())  # Create clans list
    print("List of clans:\n", clansList)
    trivialClansList = Clan.trivialClans(clansList, Graph.getMaxCardinalityFromGraph(graph))  # Create trivial clans
    # list
    # TODO cardinality ha de ser una funció de la classe Graph
    print("List of trivial clans:\n", trivialClansList)
    primalClansList = Clan.primalClans(clansList)  # Create primal clans list
    print("List of primal clans:\n", primalClansList)
    primalClansDict = Clan.primalClansDict(primalClansList)  # Create primal clans dictionary
    print("Dictionary of primal clans:\n", primalClansDict)


if __name__ == "__main__":
    graph = simpleGraph_1()  # Create a simple graph
    print("Simple graph\n")
    printResults(graph)

    graph = simpleGraph_2()  # Create a simple graph
    print("\nSimple graph\n")
    printResults(graph)

    file = str(six.moves.input("Please enter the name from SQLite file:\n"))
    connection, cursor = Data.connectionDB(file)  # Connection to SQLite database
    tableName = str(six.moves.input("Please enter the table name which to create graph: \n"))
    initGraph, rows = Graph.initGraph(tableName, cursor)  # Initialize the initGraph

    plainGraph = Graph.createPlainGraph(initGraph, rows)  # Create plain graph
    print("\nPlain graph\n")
    printResults(plainGraph)

    plainGraphWithThreshold = Graph.createPlainGraphWithThreshold(initGraph, rows, 3)  # Create a plain graph with
    # threshold
    print("\nPlain graph with threshold\n")
    printResults(plainGraphWithThreshold)

    linearGraph = Graph.createLinearGraph(initGraph, rows)  # Create linear graph
    print("\nLinear graph\n")
    printResults(linearGraph)

    exponentialGraph = Graph.createExponentialGraph(initGraph, rows)  # Create exponential graph
    print("\nExponential graph\n")
    printResults(exponentialGraph)
