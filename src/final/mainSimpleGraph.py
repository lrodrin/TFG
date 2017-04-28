"""
This module implements a main for the Graph class and test the class with a simple graphs

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
from src.final.Interface import *
from src.final.simpleGraphs import *

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

if __name__ == '__main__':
    graph = simpleGraph_1()  # Create a simple graph
    graphName = "simpleGraph1_graph.dot"
    Graph.exportGraph(graph, graphName)  # Export graph to DOT format
    Interface.openGraphviz(graphName)  # Open graph in Graphviz program

    graph = simpleGraph_2()  # Create a simple graph
    graphName = "simpleGraph2_graph.dot"
    Graph.exportGraph(graph, graphName)  # Export graph to DOT format
    Interface.openGraphviz(graphName)  # Open graph in Graphviz program
