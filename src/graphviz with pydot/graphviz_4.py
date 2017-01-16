"""
This module implements ...

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
import networkx as nx

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

clansList = [{'E'}, {'B'}, {'A'}, {'C'}, {'D'}, {'E', 'D'}, {'E', 'A', 'D'}, {'E', 'B', 'A', 'D'},
             {'E', 'B', 'A', 'C', 'D'}]

primalList =[{'D', 'E'}, {'D', 'A', 'E'}, {'B', 'D', 'A', 'E'}]

G = nx.DiGraph()

for i in range(len(clansList)):
    for j in range(i + 1, len(clansList)):
        if clansList[i] < clansList[j]:
            G.add_edge(frozenset(clansList[j]), frozenset(clansList[i]))

# write dot file to use with graphviz
nx.nx_pydot.write_dot(G, 'graphviz_4.dot')