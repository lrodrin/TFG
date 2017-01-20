"""
This module implements the main for T class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
from src.final.T import T

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

if __name__ == "__main__":
    clansList = [{'C'}, {'A'}, {'E'}, {'D'}, {'B'}, {'E', 'D'}, {'D', 'E', 'A'}, {'D', 'E', 'A', 'B'},
                 {'D', 'B', 'E', 'A',
                  'C'}]
    edgesAtributtes = {('E', 'B'): 'red', ('B', 'A'): 'red', ('C', 'B'): 'black', ('D', 'A'): 'blue', ('D', 'E'): 'red',
                       ('E', 'A'): 'blue', ('D', 'C'): 'black', ('D', 'B'): 'red', ('C', 'A'): 'black',
                       ('C', 'E'): 'black'}
      # Create a T-structureT.createTestructure(clansList, edgesAtributtes)