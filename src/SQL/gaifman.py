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

G = nx.Graph()

for row in c.execute("SELECT outlook FROM test"):
   print(row)

nx.draw(G)
plt.show()