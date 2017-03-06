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
            Graph.createPlanarGraph(graph, rows)
            Interface.openGraphviz('', 'planarGraph.dot')
        elif option == 2:
            Graph.createLinearGraph(graph, rows)
        elif option == 3:
            Graph.createExponentialGraph(graph, rows)

    @staticmethod
    def openGraphviz(program, filename):
        """
        Call the Graphviz program that is associated with a DOT file

        :param program:
        :param filename:
        """
        if sys.platform == 'win32':  # Windows platform
            os.startfile(filename)
        else:  # Linux platform
            subprocess.run(['open', '-a', program, filename])
