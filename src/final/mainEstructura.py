"""
This module implements the main for T class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
import networkx as nx
import src.final.Estructura as e
from collections import OrderedDict
from operator import itemgetter

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

if __name__ == "__main__":
    primalsList = [{'A'}, {'B'}, {'D'}, {'C'}, {'E'}, {'E', 'D'}, {'A', 'D', 'E'}, {'A', 'B', 'D', 'E'},
                   {'A', 'B', 'D', 'C', 'E'}]  # First list of primal clans
    edgesAtributtesfromGraph = {('A', 'B'): 'red', ('A', 'C'): 'black', ('B', 'E'): 'red', ('B', 'D'): 'red',
                                ('E', 'C'): 'black', ('D', 'E'): 'red', ('A', 'E'): 'blue', ('A', 'D'): 'blue',
                                ('D', 'C'): 'black', ('B', 'C'): 'black'}
    # Dictionary that contains the edges atributtes from a graph Graph

    G = nx.Graph()  # Create an empty graph structure (a “null graph”) with no nodes and no edges
    # Adding edges and edges attributes

    primalsList2 = [{'F'}, {'E'}, {'D'}, {'A'}, {'B'}, {'C'}, {'A', 'B'}, {'C', 'D'}, {'A', 'B', 'C', 'D', 'E', 'F'}]
    # Second list of primal clans
    # edgesAtributtesfromGraph

    primalsDict = OrderedDict(reversed(sorted(e.Estructura.primalSubsets(primalsList).items(), key=itemgetter(1))))
    print(primalsDict)  # First list of dict of primal clans
    primalsDict2 = OrderedDict(reversed(sorted(e.Estructura.primalSubsets(primalsList2).items(), key=itemgetter(1))))
    print(primalsDict2)  # Second list of dict of primal clans
    print("-" * 20)

    print("Get color from {'E', 'A', 'D', 'B'} and {'C'}:", (e.Estructura.getColorClans(edgesAtributtesfromGraph,
                                                                                        {'E', 'A', 'D', 'B'}, {'C'})))
    # print("Get color from {'A', 'B'} and {'F'}:", (e.Estructura.getColorClans(edgesAtributtesfromGraph2,
    # {'A', 'B'}, {'F'})))
    print("-" * 20)

    print("Creating a 2-structure...")
    e.Estructura.create_2structure(edgesAtributtesfromGraph, primalsDict)
    # print("Creating a 2-structure...")
    # e.Estructura.create_2structure(edgesAtributtesfromGraph2, primalsDict2)
