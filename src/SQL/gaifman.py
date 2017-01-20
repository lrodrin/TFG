"""
This module implements a Gaifman graph

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
import itertools
import sqlite3
import networkx as nx

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

connection = sqlite3.connect('C:/Users/Laura/PycharmProjects/TFG/src/SQL/ex_py_s.db')
cur = connection.cursor()
cur.execute('SELECT * FROM test')

colNames = [description[0] for description in cur.description]
rows = cur.fetchall()

G = nx.Graph()

# nodes
for i in range(0, len(colNames)):
    for row in rows:
        # G.add_node("%s|%s" % (colNames[i], row[i]))
        G.add_node(row[i])

# arestes
# ignorar repetits
# inicialitzacio
for (u, v) in itertools.combinations(G.nodes(), 2):
    G.add_edge(u, v, color='gray')

for row in rows:
    for (u, v) in itertools.combinations(row, 2):
        G.add_edge(u, v, color='black')

# no ignorem repetits
# comptem quants repetits

# arestes
d = dict()
for row in rows:
    for (u, v) in itertools.combinations(row, 2):
        if (u, v) in d.keys():
            d[(u, v)] = d.get((u, v)) + 1
            G.edge[u][v]['label'] += 1
        else:
            d[(u, v)] = 1
            G.edge[u][v]['label'] = 1


colors = {0: 'blue', 1: 'brown', 2: 'cyan', 3: 'green', 4: 'magenta', 5: 'orange', 6: 'purple', 7: 'red', 8: 'yellow'}


nx.nx_pydot.write_dot(G, 'gaifman.dot')

cur.close()
connection.close()
