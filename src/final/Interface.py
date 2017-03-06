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
    def graphOptions(option, graph, rows):
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
    def structureOptions(option, graph, primalClansDict):
        if option == 1:
            Estructura.create2structure(Graph.createDictFromGraph(graph), primalClansDict, 'plain2structure.dot')
        elif option == 2:
            Estructura.create2structure(Graph.createDictFromGraph(graph), primalClansDict, 'linear2structure.dot')
        elif option == 3:
            Estructura.create2structure(Graph.createDictFromGraph(graph), primalClansDict, 'exponential2structure.dot')

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
            subprocess.run(['open', '-a', sysPlatform, filename])
