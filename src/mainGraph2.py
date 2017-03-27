"""
This module implements the main for Graph class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
from src.Graph2 import *

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

if __name__ == "__main__":
    # Data input from STDIN
    nnodes = int(input("Please enter a number of nodes: "))
    ncolors = int(input("Please enter a number of colors: "))
    colorList = ['blue', 'brown', 'cyan', 'green', 'magenta', 'orange', 'purple', 'red', 'yellow']
    if ncolors > len(colorList):  # Verifying data input
        print("Ups! It is not a valid number. The number of colors may not be greater than 9! Try it again ...")
        ncolors = int(input("Please enter a number of colors: "))

    print("Creating and coloring initGraph...")
    G = Graph.creating_and_coloring_graph(nnodes=nnodes, nequivalences=ncolors, colorList=colorList)
    print("Create dot file from initGraph...")
    Graph.create_dot_file_from_graph(G, 'Graph_2.dot')
    print("Dictionary of the initGraph:\n", Graph.createDictFromGraph(G))
    print("-" * 20)
