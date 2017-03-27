"""
This module implements the main for Clan class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
import six

from src.final.Clan import *
from src.final.Graph import *
from src.simple_graphs import *

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'


def printResults(graph):
    """
    Print the results of the main execution:
        - A list of clans
        - A list of trivial clans
        - A list of primal clans
        - A dictionary of primal clans

    :param graph: Networkx's initGraph
    """
    clansList = Clan.clans(graph, graph.nodes())  # Create clans list
    print("List of clans:\n", clansList)
    trivialClansList = Clan.trivialClans(graph.nodes(), nx.graph_clique_number(graph))  # Create trivial clans list
    print("List of trivial clans:\n", trivialClansList)
    primalClansList = Clan.primalClans(clansList)  # Create primal clans list
    print("List of primal clans:\n", primalClansList)
    primalClansDict = Clan.primalClansDict(primalClansList)  # Create primal clans dictionary
    print("Dictionary of primal clans:\n", primalClansDict)


if __name__ == "__main__":
    initGraph = simpleGraph()  # Create a simple graph
    printResults(initGraph)

    file = str(six.moves.input("Please enter the name from SQLite file:\n"))
    connection, cursor = Data.connection(file)  # Connection to SQLite database
    tableName = str(six.moves.input("Please enter the table name which to create initGraph: \n"))
    initGraph, rows = Graph.initializeGraph(tableName, cursor)  # Initialize the initGraph

    plainGraph = Graph.createPlainGraph(initGraph, rows)  # Create plain graph
    printResults(plainGraph)
    linearGraph = Graph.createLinearGraph(initGraph, rows)  # Create linear graph
    printResults(linearGraph)
    exponentialGraph = Graph.createExponentialGraph(initGraph, rows)  # Create exponential graph
    printResults(exponentialGraph)
