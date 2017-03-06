"""
This module implements the main for Interface class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
from src.final.Interface import *
from src.final.Graph import *

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

if __name__ == '__main__':
    # 'C:/Users/Laura/PycharmProjects/TFG/src/SQL/BD.db'  # WINDOWS
    # '/Users/laura/PycharmProjects/TFG/src/SQL/BD.db'    # OS X
    tableName = str(input("Please enter a name for the database table: "))
    graph, rows = Graph.createGraph('C:/Users/Laura/PycharmProjects/TFG/src/SQL/BD.db', tableName)

    option = int(input("Please enter the option of graph you want to create:\n [1] = planar\n [2] = linear\n [3] "
                       "= exponential\n"))

    Interface.graphOptions(option, graph, rows)
    # Interface.openGraphviz('/Applications/Graphviz.app', 'Estructura.dot')  # OS X
    # Interface.openGraphviz('', 'planarGraph.dot')  # WINDOWS
