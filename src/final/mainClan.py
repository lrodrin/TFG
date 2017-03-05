"""
This module implements the main for Clan class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
import networkx as nx

from src.final.Clan import *

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

if __name__ == "__main__":
    graph = nx.Graph()  # Create an empty graph structure (a “null graph”) with no nodes and no edges
    # Adding edges and edges attributes
    graph.add_edges_from([('A', 'B'), ('B', 'D'), ('B', 'E'), ('D', 'E')], color='red')
    graph.add_edges_from([('A', 'C'), ('B', 'C'), ('C', 'D'), ('C', 'E')], color='black')
    graph.add_edges_from([('A', 'D'), ('A', 'E')], color='blue')

    clansList = Clan.clans(graph, set(graph.nodes()))
    print("List of clans:\n", clansList)

    trivialClansList = Clan.trivialClans(set(graph.nodes()), nx.graph_clique_number(graph))
    print("List of trivial clans:\n", trivialClansList)

    primalClansList = Clan.primalClans(clansList)
    print("List of primal clans:\n", primalClansList)
