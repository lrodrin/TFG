"""
This module implements the main for Estructura class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
from src.final.Estructura import *

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

if __name__ == "__main__":
    primalsList_1 = [frozenset({'B'}), frozenset({'A'}), frozenset({'D'}), frozenset({'C'}), frozenset({'E'}),
                     frozenset({'E', 'D'}), frozenset({'A', 'E', 'D'}), frozenset({'A', 'E', 'D', 'B'}),
                     frozenset({'A', 'E', 'D', 'C', 'B'})]
    primalsList_2 = [frozenset({'C'}), frozenset({'A'}), frozenset({'D'}), frozenset({'F'}), frozenset({'E'}),
                     frozenset({'B'}), frozenset({'D', 'C'}), frozenset({'B', 'A'}),
                     frozenset({'D', 'B', 'E', 'F', 'C', 'A'})]

    edgesAtributtesfromGraph_1 = {('C', 'B'): 'black', ('B', 'A'): 'red', ('D', 'A'): 'blue', ('E', 'A'): 'blue',
                                  ('C', 'A'): 'black', ('E', 'C'): 'black', ('D', 'B'): 'red', ('E', 'B'): 'red',
                                  ('E', 'D'): 'red', ('C', 'D'): 'black'}
    edgesAtributtesfromGraph_2 = {('D', 'C'): 'red', ('B', 'C'): 'black', ('F', 'C'): 'blue', ('D', 'A'): 'black',
                                  ('E', 'A'): 'black', ('B', 'A'): 'black', ('D', 'B'): 'black', ('B', 'E'): 'black',
                                  ('A', 'C'): 'black', ('E', 'C'): 'orange', ('D', 'E'): 'orange', ('D', 'F'): 'blue',
                                  ('A', 'F'): 'green', ('E', 'F'): 'red', ('B', 'F'): 'green'}

    primalsDict_1 = OrderedDict(reversed(sorted(Clan.primalClansSubsets(primalsList_1).items(),
                                                key=lambda t: len(t[0]))))
    primalsDict_2 = OrderedDict(reversed(sorted(Clan.primalClansSubsets(primalsList_2).items(),
                                                key=lambda t: len(t[0]))))

    print("First primals list:\n", primalsDict_1)
    print("Second primals list:\n", primalsDict_2)

    Estructura.create2structure(edgesAtributtesfromGraph_1, primalsDict_1, 'Estructura.dot')
    Estructura.create2structure(edgesAtributtesfromGraph_2, primalsDict_2, 'Estructura2.dot')

    # TODO proves planar2structure, linear2structure i exponential2structure
    tableName = str(input("Please enter a name for the database table: "))
    planarGraph, rows = Graph.graphInitialization('C:/Users/Laura/PycharmProjects/TFG/src/SQL/BD.db', tableName)
    linearGraph, rows = Graph.graphInitialization('C:/Users/Laura/PycharmProjects/TFG/src/SQL/BD.db', tableName)
    Estructura.planar2structure(planarGraph, planarGraph.nodes())
    Estructura.linear2structure(linearGraph, linearGraph.nodes())
