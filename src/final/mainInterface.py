"""
This module implements the main for Interface class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
from src.final.Interface import *

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

if __name__ == '__main__':
    # 'C:/Users/Laura/PycharmProjects/TFG/src/data/BD.db'  # WINDOWS
    # '/Users/laura/PycharmProjects/TFG/src/data/BD.db'    # OS X
    tableName = str(input("Please enter a name for the database table: "))
    graph, rows = Graph.initializeGraph('/Users/laura/PycharmProjects/TFG/src/data/BD.db', tableName)

    option = int(input("Please enter the option of graph you want to create:\n [1] = plain\n [2] = linear\n [3] "
                       "= exponential\n"))

    Interface.graphOptions(option, graph, rows, sys.platform)
    Interface.structureOptions(option, graph, rows, sys.platform)
