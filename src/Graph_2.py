"""
This module implements the Graph class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
import networkx as nx
import itertools
from numpy import random

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'


class Graph:
    G = nx.Graph()

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
    def create_dot_file_from_graph(graph, name):
        """
            Create DOT file for a Graph

        :param name: Name for DOT file
        :param graph: NetworkX's Graph
        :type graph: nx.Graph
        :type name: str
        :return: Graph in Graphviz dot format
        :rtype: DOT file
        """
        nx.nx_pydot.write_dot(graph, name)  # export Graph in Graphviz dot format

    @staticmethod
    def createDictFromGraph(graph):
        """
            Return a dictionary of attributes keyed by edge from a Graph

        :param graph:
        :return dictionary
        :rtype: dict
        """
        dictionary = nx.get_edge_attributes(graph, 'color')
        return dictionary

    @staticmethod
    def addNodes(graph, colNames, rows):
        for i in range(0, len(colNames)):
            for row in rows:
                graph.add_node(row[i])

    @staticmethod
    def initialization(graph):
        for (u, v) in itertools.combinations(graph.nodes(), 2):
            graph.add_edge(u, v, color='white')

    @staticmethod
    def plainGraph(graph, rows):
        for row in rows:
            for (u, v) in itertools.combinations(row, 2):
                graph.add_edge(u, v, color='black')
        return graph, Graph.create_dot_file_from_graph(graph, 'planar.dot')

    @staticmethod
    def linearGraph(graph, rows):
        # labeling edges
        d = dict()
        for row in rows:
            for (u, v) in itertools.combinations(row, 2):
                if (u, v) in d.keys():
                    d[(u, v)] = d.get((u, v)) + 1
                    graph.edge[u][v]['label'] += 1
                else:
                    d[(u, v)] = 1
                    graph.edge[u][v]['label'] = 1

        # painting edges by label
        colors = {0: 'white', 1: 'black', 2: 'cyan', 3: 'green', 4: 'magenta', 5: 'orange', 6: 'purple', 7: 'red',
                  8: 'yellow',
                  9: 'brown'}
        for key, value in colors.items():
            for u, v in graph.edges():
                if 'label' in graph[u][v] and key == graph[u][v]['label']:
                    graph[u][v]['color'] = value

        # TODO s'han d'amagar els labels
        return graph, Graph.create_dot_file_from_graph(graph, 'linear.dot')

    @staticmethod
    def exponentialGraph(graph, rows):
        pass