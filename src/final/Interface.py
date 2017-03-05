"""
This module implements the Interface class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'


@staticmethod
def graphOptions(option, graph, rows):
    if option == 1:
        g.Graph.planarGraph(graph, rows)
    elif option == 2:
        g.Graph.linearGraph(graph, rows)
    elif option == 3:
        g.Graph.exponentialGraph(graph, rows)