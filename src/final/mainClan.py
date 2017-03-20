"""
This module implements the main for Clan class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
from src.final.Clan import *
from src.final.Graph import *

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

if __name__ == "__main__":
    graph = nx.Graph()  # Create an empty graph structure (a null graph) with no nodes and no edges
    # Adding edges and edges attributes
    graph.add_edges_from([('A', 'B'), ('B', 'D'), ('B', 'E'), ('D', 'E')], color='white')
    graph.add_edges_from([('A', 'C'), ('B', 'C'), ('C', 'D'), ('C', 'E')], color='black')
    graph.add_edges_from([('A', 'D'), ('A', 'E')], color='blue')

    clansList = Clan.clans(graph, graph.nodes())
    print("List of clans:\n", clansList)

    trivialClansList = Clan.trivialClans(graph.nodes(), nx.graph_clique_number(graph))
    print("List of trivial clans:\n", trivialClansList)

    primalClansList = Clan.primalClans(clansList)
    print("List of primal clans:\n", primalClansList)

    primalClansDict = Clan.primalClansDict(primalClansList)
    print("Dictionary of primal clans:\n", primalClansDict)

    file = str(input("Please enter the name from SQLite file:\n"))
    connection, cursor = Data.connection(file)  # Connection to SQLite database
    tableName = str(input("Please enter the table name: \n"))
    graph, rows = Graph.initializeGraph(tableName, cursor)  # Initialize the graph
    plainGraph = Graph.createPlainGraph(graph, rows)  # Create plain graph
    # linearGraph = Graph.createLinearGraph(graph, rows)    # Create linear graph
    # exponentialGraph = Graph.createExponentialGraph(graph, rows)  # Create exponential graph

    clansList = Clan.clans(plainGraph, plainGraph.nodes())
    print("List of clans:\n", clansList)

    trivialClansList = Clan.trivialClans(plainGraph.nodes(), nx.graph_clique_number(plainGraph))
    print("List of trivial clans:\n", trivialClansList)

    primalClansList = Clan.primalClans(clansList)
    print("List of primal clans:\n", primalClansList)

    primalClansDict = Clan.primalClansDict(primalClansList)
    print("Dictionary of primal clans:\n", primalClansDict)
