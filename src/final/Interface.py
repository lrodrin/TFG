"""
This module implements the Interface class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
import os
import subprocess
import sys
from src.final.Graph import *

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'


class Interface:
    @staticmethod
    def graphOptions(option, graph, rows):
        if option == 1:
            Graph.createPlainGraph(graph, rows)
            Interface.openGraphviz(sys.platform, 'plainGraph.dot')
        elif option == 2:
            Graph.createLinearGraph(graph, rows)
            Interface.openGraphviz(sys.platform, 'linearGraph.dot')
        elif option == 3:
            Graph.createExponentialGraph(graph, rows)
            Interface.openGraphviz(sys.platform, 'exponentialGraph.dot')

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
