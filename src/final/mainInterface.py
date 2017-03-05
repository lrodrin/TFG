"""
This module implements the main for Interface class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

graphType = int(input("Please enter the option of graph you want to create:\n [1] = planar\n [2] = linear\n [3] "
                          "= exponential\n"))
    graph = g.Graph.G
    g.Graph.addNodes(graph, columnNames, rows)  # add nodes
    d.Data.graphOptions(graphType, graph, rows)

    print("Open Graphviz program...")
    # e.Estructura.openGraphviz('/Applications/Graphviz.app', 'Estructura.dot')  # OS X
    e.Estructura.openGraphviz('', 'Estructura.dot')  # WINDOWS
    d.Data.close(file, cursor, connection)
