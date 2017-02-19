"""
This module implements the main for Estructura class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
from collections import OrderedDict
from operator import itemgetter
import src.final.Estructura as e

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

if __name__ == "__main__":
    primalsList = [{'E'}, {'C'}, {'A'}, {'B'}, {'D'}, {'E', 'D'}, {'E', 'D', 'A'}, {'E', 'D', 'B', 'A'},
                   {'E', 'C', 'D', 'B', 'A'}]
    primalsListFrozen = [frozenset({'E', 'D', 'A'}), frozenset({'A'}), frozenset({'B'}),
                         frozenset({'E', 'C', 'D', 'B', 'A'}), frozenset({'C'}), frozenset({'E', 'D'}),
                         frozenset({'D'}), frozenset({'E', 'D', 'B', 'A'}), frozenset({'E'})]

    edgesAtributtesfromGraph = {('C', 'B'): 'black', ('B', 'A'): 'red', ('D', 'A'): 'blue', ('E', 'A'): 'blue',
                                ('C', 'A'): 'black', ('E', 'C'): 'black', ('D', 'B'): 'red', ('E', 'B'): 'red',
                                ('E', 'D'): 'red', ('C', 'D'): 'black'}
    print(sorted(primalsList))
    primalsDict = OrderedDict(reversed(sorted(e.Estructura.primalSubsets(sorted(primalsList)).items(), key=itemgetter(1))))
    primalsDictFrozen = OrderedDict(reversed(sorted(e.Estructura.primalSubsets(sorted(primalsListFrozen)).items(),
                                                    key=itemgetter(1))))
    print(primalsDict)
    print(primalsDictFrozen)
    # print("-" * 20)

    # print("Get color from {'E', 'A', 'D', 'B'} and {'C'}:", (e.Estructura.getColorClans(edgesAtributtesfromGraph,
    #                                                                                     {'E', 'A', 'D', 'B'}, {'C'})))
    # print("Get color from {'A', 'B'} and {'F'}:", (e.Estructura.getColorClans(edgesAtributtesfromGraph2,
    #                                                                           {'A', 'B'}, {'F'})))
    # print("-" * 20)

    print("Creating a 2-structure...")
    e.Estructura.create_2structure(edgesAtributtesfromGraph, primalsDict)
    # print("Creating a 2-structure...")
    # e.Estructura.create_2structure(edgesAtributtesfromGraph2, primalsDict2)
