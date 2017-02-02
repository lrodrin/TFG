"""
This module implements the main for Clan class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
import networkx as nx
import src.iter_subsets as it
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

    subsetNodes = set(G.nodes())  # Subset of nodes from G
    cardinality = nx.graph_clique_number(G)  # A maximal cardinality matching in the graph

    clansList = []
    for s in it.powerset_generator(subsetNodes):  # Subset iterator of each subsetNodes
        if c.Clan.clans(G, s):  # If s is a clan of G
            clansList.append(s)  # Add s to the list
    print("Complete list of clans:\n", sorted(clansList))  # Complete list of clans sorted by len
    print("-" * 20)

    clansList_2 = []
    for s in it.powerset_generator(subsetNodes):  # Subset iterator of each subsetNodes
        if c.Clan.clans(G, s) and not c.Clan.trivialClans(s, cardinality):
            # If s is a clan of G and isn't a trivial clan
            clansList_2.append(s)  # Add s to the list
    print("Complete list of clans less trivial clans:\n", sorted(clansList_2))  # Complete list of clans less trivial
    #  clans sorted by len
    print("-" * 20)

    # print("Complete list of primal clans:\n", c.Clan.primalClans(clansList_2))
    # print("-" * 20)
    print("Complete list of primal clans less trivial clans:\n", c.Clan.primalClans(clansList_2))
    print("-" * 20)

    print(g.Graph.create_dict_from_graph(G))

    for key, value in g.Graph.create_dict_from_graph(G).items():
        if c.Clan.clans(G, key):
            print(value)