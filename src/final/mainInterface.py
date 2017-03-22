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
    fileOption = int(six.moves.input("Please enter the option for the file you provide:\n [1] = .arff\n [2] = .db\n"))
    cursor = Interface.fileOptions(fileOption)

    tableName = str(six.moves.input("Please enter the table name: \n"))
    graph, rows = Graph.initializeGraph(tableName, cursor)  # Initialize the graph

    # option = int(six.moves.input("Please enter the option of graph you want to create:\n [1] = plain\n [2] = plain
    # with " "threshold\n [3] = linear\n [4] = exponential\n")) Interface.graphOptions(option, graph, rows)

    option = int(six.moves.input("Please enter the option of 2-structure you want to create:\n [1] = plain\n [2] = "
                                 "linear\n [3] = exponential\n"))
    # Interface.structureOptions(option, graph, rows)
    Interface.graphANDstructureOptions(option, graph, rows)
