"""
This module implements the Interface class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
import os
import subprocess
import sys

from src.final.Estructura import *

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'


class Interface:
    @staticmethod
    def graphOptions(option, graph, rows, sysPlatform):
        if option == 1:
            Graph.createPlainGraph(graph, rows)
            filename = 'plainGraph.dot'
            Graph.exportGraphDOT(graph, filename)
            Interface.openGraphviz(sys.platform, filename)
        elif option == 2:
            Graph.createLinearGraph(graph, rows)
            filename = 'linearGraph.dot'
            Graph.exportGraphDOT(graph, filename)
            Interface.openGraphviz(sys.platform, filename)
        elif option == 3:
            Graph.createExponentialGraph(graph, rows)
            filename = 'exponentialGraph.dot'
            Graph.exportGraphDOT(graph, filename)
            Interface.openGraphviz(sys.platform, filename)

    @staticmethod
    def structureOptions(option, graph, rows, sysPlatform):
        if option == 1:
            plainGraph = Graph.createPlainGraph(graph, rows)
            Estructura.plain2structure(plainGraph, plainGraph.nodes())
            Interface.openGraphviz(sys.platform, 'plain2structure.dot')
        elif option == 2:
            linearGraph = Graph.createLinearGraph(graph, rows)
            Estructura.linear2structure(linearGraph, linearGraph.nodes())
            Interface.openGraphviz(sys.platform, 'linear2structure.dot')
        elif option == 3:
            exponentialGraph = Graph.createExponentialGraph(graph, rows)
            Estructura.exponential2structure(exponentialGraph, exponentialGraph.nodes())
            Interface.openGraphviz(sys.platform, 'exponential2structure.dot')

    @staticmethod
    def openGraphviz(sysPlatform, filename):
        """
        Call the Graphviz program that is associated with a DOT file

        :param sysPlatform:
        :param filename: DOT file
        :type sysPlatform: str
        :type filename: str
        """
        if sys.platform == 'win32':  # Windows platform
            os.startfile(filename)
        else:  # Linux platform
            subprocess.run(['open', '-a', 'Graphviz.app', filename])
