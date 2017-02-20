"""
This module implements a Gaifman graph

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
import itertools
from collections import OrderedDict

import networkx as nx

import src.final.Clan as c
import src.final.Data as d
import src.final.Estructura as e
import src.final.Graph as g

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

pathBD = str(input("Please enter a path from database file: "))
# C:/Users/Laura/PycharmProjects/TFG/src/SQL/BD.db
connection = d.Data.connection(pathBD)
cursor = connection.cursor()

cursor.execute('SELECT * FROM test2')
colNames = [description[0] for description in cursor.description]
rows = cursor.fetchall()

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
    G.add_edge(u, v, color='white')

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

colors = {0: 'white', 1: 'black', 2: 'cyan', 3: 'green', 4: 'magenta', 5: 'orange', 6: 'purple', 7: 'red', 8: 'yellow',
          9: 'brown'}
for key, value in colors.items():
    for u, v in G.edges():
        if 'label' in G[u][v] and key == G[u][v]['label']:
            G[u][v]['color'] = value

nx.nx_pydot.write_dot(G, 'gaifman.dot')

clansList = c.Clan.clans(G, set(G.nodes()))
print("List of clans:\n", clansList)
print("-" * 20)

primalsList = c.Clan.primalClans(clansList)
print("List of primal clans:\n", primalsList)
print("-" * 20)

edgesAtributtesfromGraph = g.Graph.create_dict_from_graph(G)
primalsDict = OrderedDict(reversed(sorted(e.primalSubsets(primalsList).items(),
                                          key=lambda t: len(t[0]))))  # dictionary sorted by length of the
# key string
e.Estructura.create_2structure(edgesAtributtesfromGraph, primalsDict, 'Estructura.dot')

cursor.close()
connection.close()
