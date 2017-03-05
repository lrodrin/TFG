"""
This module implements a Gaifman graph from database and create a 2-structure of this graph

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
import itertools
# import os
import sqlite3
from collections import OrderedDict
import networkx as nx
import src.final.Clan as c
import src.final.Estructura as e
import src.final.Graph as g

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

# global variables
connection = ""
file = ""
query = ""
colNames = ""
values = ""

try:
    # connection = sqlite3.connect('C:/Users/Laura/PycharmProjects/TFG/src/SQL/BD.db')  # Connection to database
    connection = sqlite3.connect('/Users/laura/PycharmProjects/TFG/src/SQL/BD.db')
except sqlite3.Error as e:
    print("Error:", e)

cur = connection.cursor()

try:
    # file = open('C:/Users/Laura/PycharmProjects/TFG/src/SQL/meteo.txt', 'r')  # Open data file
    file = open('/Users/laura/PycharmProjects/TFG/src/SQL/meteo.txt', 'r')  # Open data file

except IOError as e:
    print("Error:", e)

lines = file.readlines()  # Keep all lines from data file into lines
header = lines[0]  # Extract the header from lines
for word in header.split(" "):  # For each word from header
    colNames += word + ", "  # Adding a column into colNames

tableName = str(input("Please enter a name for the database table: "))
try:
    query = "CREATE TABLE %s (%s);" % (str(tableName), str(colNames[0:-2]))  # Create a table
    # cur.execute(query)
    print("Created table %s..." % tableName)
except sqlite3.Error as e:
    print("Error:", e)

for i in range(1, len(lines)):  # For each row from data file
    for col in lines[i].split(" "):  # For each column in lines[i]
        values += "'%s'," % col.split(":")[1]  # Extract and save the value
    try:
        query = 'INSERT INTO {0} ({1}) VALUES ({2});'.format(str(tableName), str(colNames[0:-2]),
                                                             str(values[0:-1]).replace('\n', ''))

        # Insert values to table
        # print(query)
        # cur.execute(query)
        # connection.commit()
        # print("Inserted row number %d" % i)
    except sqlite3.Error as e:
        print("Error:", e)
    values = ""

cur.execute("SELECT * FROM %s" % tableName)
colNames = [description[0] for description in cur.description]
rows = cur.fetchall()

G = nx.Graph()
# nodes
for i in range(0, len(colNames)):
    for row in rows:
        G.add_node(row[i])

# arestes
# inicialitzacio
for (u, v) in itertools.combinations(G.nodes(), 2):
    G.add_edge(u, v, color='white')

# no repetits
for row in rows:
    for (u, v) in itertools.combinations(row, 2):
        G.add_edge(u, v, color='black')

# repetits
# comptem quants repetits
# etiquetar arestes
d = dict()
for row in rows:
    for (u, v) in itertools.combinations(row, 2):
        if (u, v) in d.keys():
            d[(u, v)] = d.get((u, v)) + 1
            G.edge[u][v]['label'] += 1
        else:
            d[(u, v)] = 1
            G.edge[u][v]['label'] = 1

# pintar arestes segons l'etiqueta
colors = {0: 'white', 1: 'black', 2: 'cyan', 3: 'green', 4: 'magenta', 5: 'orange', 6: 'purple', 7: 'red', 8: 'yellow',
          9: 'brown'}
for key, value in colors.items():
    for u, v in G.edges():
        if 'label' in G[u][v] and key == G[u][v]['label']:
            G[u][v]['color'] = value

nx.nx_pydot.write_dot(G, 'gaifman.dot')

# clans
clansList = clans(G, set(G.nodes()))
print("List of clans:\n", clansList)
print("-" * 20)

# clans primers
primalsList = primalClans(clansList)
print("List of primal clans:\n", primalsList)
print("-" * 20)

edgesAtributtesfromGraph = g.Graph.create_dict_from_graph(G)
primalsDict = OrderedDict(reversed(sorted(e.Estructura.primalSubsets(primalsList).items(),
                                          key=lambda t: len(t[0]))))
print("Dict of primal clans:\n", primalsDict)
print("-" * 20)

e.Estructura.create_2structure(edgesAtributtesfromGraph, primalsDict, 'Estructura.dot')
# e.Estructura.openGraphviz('/Applications/Graphviz.app', 'Estructura.dot')  # OS X
# e.Estructura.openGraphviz('', 'Estructura.dot')  # WINDOWS

file.close()
cur.close()
connection.close()
