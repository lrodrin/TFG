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
    fileOption = int(input("Please enter the option for the file you provide:\n [1] = .arff\n [2] = .db\n"))
    cursor = Interface.fileOptions(fileOption)

    tableName = str(input("Table name: \n"))
    graph, rows = Graph.initializeGraph(tableName, cursor)

    # option = int(input("Please enter the option of graph you want to create:\n [1] = plain\n [2] = linear\n [3] "
    # "= exponential\n [4] = plain with threshold\n")) Interface.graphOptions(option, graph, rows) option = int(
    # input("Please enter the option of 2-structure you want to create:\n [1] = plain\n [2] = linear\n [3] " "=
    # exponential\n")) Interface.structureOptions(option, graph, rows)
    option = int(input("Please enter the option of graph and structure you want to create:\n [1] = plain\n [2] = "
                       "linear\n [3] = exponential\n"))
    Interface.graphAndstructureOptions(option, graph, rows)
