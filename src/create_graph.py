"""
This module implements ...

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
import networkx as nx
import src.final.Subset as it
import src.final.Clan as c
import src.final.Graph as g

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'


if __name__ == "__main__":

    G = nx.Graph()  # Create an empty graph structure (a “null graph”) with no nodes and no edges
    # Adding edges and edges attributes
    G.add_edges_from([('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'E'), ('B', 'C'), ('B', 'D'), ('B', 'E')],
                     color='black')
    G.add_edges_from([('C', 'F'), ('D', 'F')], color='blue')
    G.add_edges_from([('C', 'D'), ('E', 'F')], color='red')
    G.add_edges_from([('A', 'F'), ('B', 'F')], color='green')
    G.add_edges_from([('C', 'E'), ('D', 'E')], color='orange')

    nx.nx_pydot.write_dot(G, 'create_graph.dot')  # Return a pydot graph from G

    setNodes = set(G.nodes())  # Set of nodes from G
    cardinality = nx.graph_clique_number(G)  # A maximal cardinality matching in the graph

    clansList = []  # Empty clans list
    for subset in it.Subset.powerset_generator(setNodes):  # Subset iterator of each set in setNodes
        if c.Clan.isClan(G, subset):  # If subset is a clan of graph G
            clansList.append(subset)  # Add subset to the clans list
    print("List of clans:\n", clansList)
    print("-" * 20)

    primalsList = c.Clan.primalClans(clansList)
    print("List of primal clans:\n", primalsList)

    print("Dictionary of the graph:\n", g.Graph.create_dict_from_graph(G))
    print("-" * 20)