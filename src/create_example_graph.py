"""
This module implements ...

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
# import random

import networkx as nx

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

if __name__ == "__main__":
    # G = nx.Graph()  # Undirected graph
    G = nx.DiGraph()    # Directed graph
    G.add_edges_from(
        [('A', 'B'), ('A', 'C'), ('D', 'B'), ('E', 'C'), ('E', 'F'),
         ('B', 'H'), ('B', 'G'), ('B', 'F'), ('C', 'G')])

    # for u, v in G.edges():  # Label edges
    #     G.edge[u][v]['label'] = random.randrange(0, 9)

    nx.nx_pydot.write_dot(G, "create_example_graph.dot")
