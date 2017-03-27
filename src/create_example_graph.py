"""
This module implements ...

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""

from src.final.Clan import *
from src.final.Graph import *

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

if __name__ == "__main__":
    G = nx.Graph()  # Create an empty initGraph structure (a “null initGraph”) with no nodes and no edges
    # Adding edges and edges attributes
    G.add_edges_from([('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'E'), ('B', 'C'), ('B', 'D'), ('B', 'E')],
                     color='black')
    G.add_edges_from([('C', 'F'), ('D', 'F')], color='blue')
    G.add_edges_from([('C', 'D'), ('E', 'F')], color='red')
    G.add_edges_from([('A', 'F'), ('B', 'F')], color='green')
    G.add_edges_from([('C', 'E'), ('D', 'E')], color='orange')

    nx.nx_pydot.write_dot(G, 'create_example_graph.dot')  # Return a pydot initGraph from initGraph

    setNodes = set(G.nodes())  # Set of nodes from initGraph
    cardinality = nx.graph_clique_number(G)  # A maximal cardinality matching in the initGraph

    clansList = Clan.clans(G, setNodes)
    print("List of clans:\n", clansList)
    print("-" * 20)

    trivialClansList = Clan.trivialClans(setNodes, cardinality)
    print("List of clans:\n", trivialClansList)
    print("-" * 20)

    primalsList = Clan.primalClans(clansList)
    print("List of primal clans:\n", primalsList)
    print("-" * 20)

    print("Dictionary of the initGraph:\n", Graph.getAttributesFromGraph(G))
    print("-" * 20)
