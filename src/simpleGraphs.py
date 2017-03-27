"""
This module implements examples of simple graphs

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
import networkx as nx

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'


def simpleGraph_1():
    """
    Create a simple Networkx's graph structure with nodes and edges adding edges attributes

    :return: A Networkx's graph
    :rtype: nx.Graph
    """
    graph = nx.Graph()  # Create an empty graph structure (a null graph) with no nodes and no edges

    # Adding edges and edges attributes
    graph.add_edges_from([('A', 'B'), ('B', 'D'), ('B', 'E'), ('D', 'E')], color='red')
    graph.add_edges_from([('A', 'C'), ('B', 'C'), ('C', 'D'), ('C', 'E')], color='black')
    graph.add_edges_from([('A', 'D'), ('A', 'E')], color='blue')

    return graph


def simpleGraph_2():
    """
    Create a simple Networkx's graph structure with nodes and edges adding edges attributes

    :return: A Networkx's graph
    :rtype: nx.Graph
    """
    graph = nx.Graph()  # Create an empty graph structure (a null graph) with no nodes and no edges

    # Adding edges and edges attributes
    graph.add_edges_from([('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'E'), ('B', 'C'), ('B', 'D'), ('B', 'E')],
                         color='black')
    graph.add_edges_from([('A', 'F'), ('B', 'F')], color='orange')
    graph.add_edges_from([('C', 'D'), ('E', 'F')], color='red')
    graph.add_edges_from([('C', 'E'), ('D', 'E')], color='green')
    graph.add_edges_from([('C', 'F'), ('D', 'F')], color='blue')

    return graph


if __name__ == '__main__':
    simpleGraph_1 = simpleGraph_1()
    nx.nx_pydot.write_dot(simpleGraph_1, 'simpleGraph 1.dot')
    simpleGraph_2 = simpleGraph_2()
    nx.nx_pydot.write_dot(simpleGraph_2, 'simpleGraph 2.dot')
