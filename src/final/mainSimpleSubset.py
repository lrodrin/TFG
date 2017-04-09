"""
This module implements a main for the Subset class and test the class with a simple graphs

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
from src.final.simpleGraphs import *
from src.final.Subset import *

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

if __name__ == '__main__':
    graph = simpleGraph_1()  # Create a simple graph
    print("Simple graph 1")
    for subset in Subset.powerSetGenerator(graph.nodes()):  # All subsets from a graph
        print(subset)

    graph = simpleGraph_2()  # Create a simple graph
    print("\nSimple graph 2")
    for subset in Subset.powerSetGenerator(graph.nodes()):  # All subsets from a graph
        print(subset)