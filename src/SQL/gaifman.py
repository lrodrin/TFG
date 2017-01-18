"""
This module implements ...

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
import sqlite3
import networkx as nx
from matplotlib import pyplot as plt

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

conn = sqlite3.connect('C:/Users/Laura/PycharmProjects/TFG/src/SQL/ex_py_s.db')
c = conn.cursor()
c.execute('SELECT * FROM test')
names = [description[0] for description in c.description]
rows = c.fetchall()

G = nx.Graph()
for row in rows:
    G.add_node("%s:%s" % (names[0], row[0]))
    G.add_node("%s:%s" % (names[1], row[1]))
    G.add_node("%s:%s" % (names[2], row[2]))
    G.add_node("%s:%s" % (names[3], row[3]))
    G.add_node("%s:%s" % (names[4], row[4]))

nx.draw(G, pos=nx.spring_layout(G), with_labels=True)
plt.show()
c.close()
conn.close()