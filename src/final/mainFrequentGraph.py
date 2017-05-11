"""
This module implements a main for the Graph class and test the class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""

from src.final.Interface import *

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

if __name__ == '__main__':
    arpFile = str(six.moves.input("Please enter a filename:\n"))
    graph = Graph.initFrequentGraph(arpFile + ".ap")
    Graph.exportGraph(graph, "frequentGraph.dot")
    Interface.openGraphviz("frequentGraph.dot")