"""
This module implements the main for Subset class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
from src.final.Subset import *
from src.simple_graphs import *

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

if __name__ == "__main__":
    initGraph = simpleGraph()  # Create a simple graph

    for subset in Subset.powersetGenerator(initGraph.nodes()):
        print(subset)
