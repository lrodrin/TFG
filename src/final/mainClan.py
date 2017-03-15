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

    primalClansSubsets = Clan.primalClansSubsets(primalClansList)
    print("List of primal clans subsets:\n", primalClansSubsets)

    file = str(input("Please enter the name from DB SQLite file:\n"))
    connection, cursor = Data.connection(file)  # Connection to SQLite database
    # C:/Users/Laura/PycharmProjects/TFG/src/final/DB.db  WINDOWS
    # /Users/laura/PycharmProjects/TFG/src/final/DB.db    OS X
    tableName = str(input("Table name: \n"))
    graph, rows = Graph.initializeGraph(tableName, cursor)
    print("init")
    plainGraph = Graph.createPlainGraph(graph, rows)
    print("graph")
    # linearGraph = Graph.createLinearGraph(graph, rows)
    # exponentialGraph = Graph.createExponentialGraph(graph, rows)

    clansList = Clan.clans(plainGraph, set(plainGraph.nodes()))
    print("List of clans:\n", clansList)

    trivialClansList = Clan.trivialClans(set(plainGraph.nodes()), nx.graph_clique_number(plainGraph))
    print("List of trivial clans:\n", trivialClansList)

    primalClansList = Clan.primalClans(clansList)
    print("List of primal clans:\n", primalClansList)
