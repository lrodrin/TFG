"""
This module implements the main for T class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
import src.final.Estructura as e

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

if __name__ == "__main__":

    primalsList = [{'A'}, {'B'}, {'D'}, {'C'}, {'E'}, {'E', 'D'}, {'A', 'D', 'E'}, {'A', 'B', 'D', 'E'},
                   {'A', 'B', 'D', 'C', 'E'}]  # List of clans
    edgesAtributtesfromGraph = {('A', 'B'): 'red', ('A', 'C'): 'black', ('B', 'E'): 'red', ('B', 'D'): 'red',
                                ('E', 'C'): 'black', ('D', 'E'): 'red', ('A', 'E'): 'blue', ('A', 'D'): 'blue',
                                ('D', 'C'): 'black', ('B', 'C'): 'black'}
    # Dictionary that contains the edges atributtes from a graph Graph

    # print("Creating a 2-structure...")
    # e.Estructura.create_2structure(primalsList, edgesAtributtesfromGraph)

    primalsList2 = [{'F'}, {'E'}, {'D'}, {'A'}, {'B'}, {'C'}, {'A', 'B'}, {'C', 'D'}, {'A', 'B', 'C', 'D', 'E', 'F'}]
    e.Estructura.nose(primalsList2)
