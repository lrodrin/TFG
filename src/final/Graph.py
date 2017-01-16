"""
This module implements the Graph class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
import networkx as nx
from numpy import random

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'


class Graph(object):
    @staticmethod
    def creating_and_coloring_graph(nnodes=None, nequivalences=None, colorList=None):
        """
            Create and give color to complete Graph

            :param nnodes: The number of nodes
            :param nequivalences: The number of colors assigned for edges
            :param colorList: List of possible colors for each edge
            :type nnodes: int
            :type nequivalences: int
            :type colorList: list
            :return: Graph in Graphviz dot format
            :rtype: dot
        """
        G = nx.nx.complete_graph(nnodes)    # Graph generator
        for (u, v) in G.edges():  # For each edge of Graph the color attribute is assigned randomly
            G.edge[u][v]['color'] = random.choice(colorList[0:nequivalences])
        nx.nx_pydot.write_dot(G, 'graph.dot')  # export Graph in Graphviz dot format