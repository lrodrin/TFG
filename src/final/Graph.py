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


class Graph:
    @staticmethod
    def creating_and_coloring_graph(nnodes=None, nequivalences=None, colorList=None):
        """
            Create and give colors to complete Graph

            :param nnodes: The number of nodes
            :param nequivalences: The number of colors assigned for edges
            :param colorList: List of possible colors for each edge
            :type nnodes: int
            :type nequivalences: int
            :type colorList: list
            :return: Complete NetworkX's Graph with nnodes and nnequivalences
            :rtype: nx.Graph
        """
        G = nx.nx.complete_graph(nnodes)    # Graph generator
        for (u, v) in G.edges():  # For each edge of Graph the color attribute is assigned randomly
            G.edge[u][v]['color'] = random.choice(colorList[0:nequivalences])
        return G

    @staticmethod
    def create_dot_file_from_graph(graph):
        """
            Create DOT file for a Graph

        :param graph: NetworkX's Graph
        :type graph: nx.Graph
        :return: Graph in Graphviz dot format
        :rtype: DOT file
        """
        nx.nx_pydot.write_dot(graph, 'Graph.dot')  # export Graph in Graphviz dot format

    @staticmethod
    def create_dict_from_graph(graph):
        """
            Return a dictionary of attributes keyed by edge from a Graph

        :param graph:
        :return dictionary
        :rtype: dict
        """
        dictionary = nx.get_edge_attributes(graph, 'color')
        return dictionary

    @staticmethod
    def planar():
        pass

    @staticmethod
    def linear():
        pass

    @staticmethod
    def exponential():
        pass