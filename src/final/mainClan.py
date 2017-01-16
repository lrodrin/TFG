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

    # clansList_1 = []
    # for s in it.all_subsets(subsetNodes):  # Subset iterator of each subsetNodes
    #     if c.Clan.isAClan(G, s):  # If s is a clan of G
    #         clansList_1.append(s)  # Add s to the list
    # print(sorted(clansList_1))  # Complete list of clans sorted by len
    # print("-" * 20)

    clansList_2 = []
    for s in it.powerset_generator(subsetNodes):  # Subset iterator of each subsetNodes
        if c.Clan.isAClan(G, s):  # If s is a clan of G
            clansList_2.append(s)  # Add s to the list
    print("Complete list of clans:\n", sorted(clansList_2))  # Complete list of clans sorted by len
    print("-" * 20)

    # clansList_3 = []
    # for s in it.all_subsets(subsetNodes):  # Subset iterator of each subsetNodes
    #     if c.Clan.isAClan(G, s) and not c.Clan.isATrivialClan(s, cardinality):
    #         # If s is a clan of G and isn't a trivial clan
    #         clansList_3.append(s)  # Add s to the list
    # print(sorted(clansList_3))  # Complete list of clans less trivial clans sorted by len
    # print("-" * 20)

    clansList_4 = []
    for s in it.powerset_generator(subsetNodes):  # Subset iterator of each subsetNodes
        if c.Clan.isAClan(G, s) and not c.Clan.isATrivialClan(s, cardinality):
            # If s is a clan of G and isn't a trivial clan
            clansList_4.append(s)  # Add s to the list
    print("Complete list of clans less trivial clans:\n", sorted(clansList_4))  # Complete list of clans less trivial
    #  clans sorted by len
    print("-" * 20)

    # print("Complete list of primal clans:\n", c.Clan.primalClans(clansList_2))
    # print("-" * 20)
    print("Complete list of primal clans less trivial clans:\n", c.Clan.primalClans(clansList_4))
    print("-" * 20)

    print(g.Graph.create_dict_from_graph(G))