"""
This module implements ...

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""

import networkx as nx

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

if __name__ == "__main__":
    nodes = 5
    G = nx.complete_graph(nodes)  # Complete graph
    nx.nx_pydot.write_dot(G, "complete_example_graph.dot")
