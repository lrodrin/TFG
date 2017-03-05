"""
This module implements the main for Clan class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
import networkx as nx
import src.final.Clan as c
import src.final.Graph as g

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'


if __name__ == "__main__":
    G = nx.Graph()  # Create an empty graph structure (a “null graph”) with no nodes and no edges
    # Adding edges and edges attributes
    G.add_edges_from([('A', 'B'), ('B', 'D'), ('B', 'E'), ('D', 'E')], color='red')
    G.add_edges_from([('A', 'C'), ('B', 'C'), ('C', 'D'), ('C', 'E')], color='black')
    G.add_edges_from([('A', 'D'), ('A', 'E')], color='blue')
    setNodes = set(G.nodes())  # Set of nodes from G
    cardinality = nx.graph_clique_number(G)  # A maximal cardinality matching in the graph

    clansList = c.Clan.clans(G, setNodes)
    print("List of clans:\n", clansList)
    print("-" * 20)

    trivialClansList = c.Clan.trivialClans(setNodes, cardinality)
    print("List of clans:\n", trivialClansList)
    print("-" * 20)

    primalsList = c.Clan.primalClans(clansList)
    print("List of primal clans:\n", primalsList)
    print("-" * 20)

    print("Dictionary of the graph:\n", g.Graph.create_dict_from_graph(G))
    print("-" * 20)