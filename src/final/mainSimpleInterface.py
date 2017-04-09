"""
This module implements a main for the Interface class and test the class with a simple graphs

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

from src.final.Interface import *
from src.final.simpleGraphs import *

if __name__ == '__main__':
    # Simple graphs
    graph = simpleGraph_1()  # Create a simple graph
    graphName = "simpleGraph1.dot"
    Graph.exportGraph(graph, graphName)  # Export graph to DOT format
    Interface.openGraphviz(graphName)  # Open graph in Graphviz program
    structureName = 'Structure.dot'
    Structure.create2Structure(graph, structureName)  # Create a 2-structure from graph
    Interface.openGraphviz(structureName)

    graph = simpleGraph_2()  # Create a simple graph
    graphName = "simpleGraph2.dot"
    Graph.exportGraph(graph, graphName)  # Export graph to DOT format
    Interface.openGraphviz(graphName)  # Open graph in Graphviz program
    structureName = 'Structure2.dot'
    Structure.create2Structure(graph, structureName)  # Create a 2-structure from graph
    Interface.openGraphviz(structureName)
