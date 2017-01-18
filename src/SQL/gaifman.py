"""
This module implements a Gaifman graph

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
import sqlite3
import networkx as nx
from matplotlib import pyplot as plt

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

connection = sqlite3.connect('C:/Users/Laura/PycharmProjects/TFG/src/SQL/ex_py_s.db')
cur = connection.cursor()
cur.execute('SELECT * FROM test')

colNames = [description[0] for description in cur.description]
rows = cur.fetchall()

G = nx.Graph()
for row in rows:
    G.add_node("%s:%s" % (colNames[0], row[0]))
    G.add_node("%s:%s" % (colNames[1], row[1]))
    G.add_node("%s:%s" % (colNames[2], row[2]))
    G.add_node("%s:%s" % (colNames[3], row[3]))
    G.add_node("%s:%s" % (colNames[4], row[4]))

# pintar blaus mateixa columna
# si name [i] == name [i+1] and value


# tots amb tots
# per a cada node si estan repetits en la mataixa fila vermell i sinó blau

nx.draw(G, pos=nx.spring_layout(G), with_labels=True, node_size=11000)
plt.show()

cur.close()
connection.close()