"""
This module implements examples of simple graphs

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
import networkx as nx

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'


def simpleGraph():
    """
    Create a simple Networkx's initGraph structure with nodes and edges adding edges attributes

    :return: A initGraph
    :rtype: nx.Graph
    """
    graph = nx.Graph()  # Create an empty initGraph structure (a null initGraph) with no nodes and no edges

    # Adding edges and edges attributes
    graph.add_edges_from([('A', 'B'), ('B', 'D'), ('B', 'E'), ('D', 'E')], color='white')
    graph.add_edges_from([('A', 'C'), ('B', 'C'), ('C', 'D'), ('C', 'E')], color='black')
    graph.add_edges_from([('A', 'D'), ('A', 'E')], color='blue')

    return graph
