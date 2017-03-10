"""
This module implements a Gaifman graph from database and create a 2-structure of this graph

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
from src.final.Graph import *

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

if __name__ == '__main__':
    # connection = sqlite3.connect('C:/Users/Laura/PycharmProjects/TFG/src/data/BD.db')  # WINDOWS
    # connection = sqlite3.connect('/Users/laura/PycharmProjects/TFG/src/data/BD.db')    # OS X
    tableName = str(input("Please enter a name for the database table: "))
    graph, rows = Graph.createGraph('/Users/laura/PycharmProjects/TFG/src/data/BD.db', tableName)

    option = int(input("Please enter the option of graph you want to create:\n [1] = plain\n [2] = linear\n [3] "
                       "= exponential\n"))

    if option == 1:
        plainGraph = Graph.createPlainGraph(graph, rows)
        Graph.exportGraphDOT(graph, 'plainGraph.dot')
    elif option == 2:
        linearGraph = Graph.createLinearGraph(graph, rows)
        Graph.exportGraphDOT(graph, 'linearGraph.dot')
    elif option == 3:
        exponentialGraph = Graph.createExponentialGraph(graph, rows)
        Graph.exportGraphDOT(graph, 'exponentialGraph.dot')
