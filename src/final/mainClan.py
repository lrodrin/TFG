"""
This module implements the main for Clan class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
import networkx as nx
import src.final.Clan as c
import src.final.Graph as g
import src.iter_subsets as it

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

    clansList = []  # Empty clans list
    for subset in it.powerset_generator(setNodes):  # Subset iterator of each set in setNodes
        if c.Clan.clans(G, subset):  # If subset is a clan of graph G
            clansList.append(subset)  # Add subset to the clans list
    print("List of clans:\n", clansList)
    print("-" * 20)

    clansList_2 = []    # Empty clans list
    for subset in it.powerset_generator(setNodes):  # Subset iterator of each set in setNodes
        if c.Clan.trivialClan(subset, cardinality):  # If subset is a trivial clan of G
            clansList_2.append(subset)  # Add subset to the list
    print("List of trivial clans:\n", clansList_2)
    print("-" * 20)

    primalsList = c.Clan.primalClans(clansList)
    print("List of primal clans:\n", primalsList)
    print("-" * 20)

    print("Lists of clans division:\n", c.Clan.listClansDivision(clansList))
    print("-" * 20)

    # TODO colors
    grafDict = g.Graph.create_dict_from_graph(G)
    print(grafDict)
    print("-" * 20)