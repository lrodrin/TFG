"""
This module implements a main for the Clan class and test the class with a simple graphs

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""

from src.final.Interface import *
from src.final.simpleGraphs import *

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

if __name__ == "__main__":
    graph = simpleGraph_1()  # Create a simple graph
    graphName = "Simple graph 1"
    print(graphName + "\n" + len(graphName) * "-")
    Clan.printResults(graph)

    graph = simpleGraph_2()  # Create a simple graph
    graphName = "Simple graph 2"
    print("\n" + graphName + "\n" + len(graphName) * "-")
    Clan.printResults(graph)
