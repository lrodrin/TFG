"""
This module implements a Gaifman graph from database and create a 2-structure of this graph

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
from src.final.Graph import *

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

# connection = sqlite3.connect('C:/Users/Laura/PycharmProjects/TFG/src/SQL/BD.db')  # WINDOWS
# connection = sqlite3.connect('/Users/laura/PycharmProjects/TFG/src/SQL/BD.db')    # OS X
tableName = str(input("Please enter a name for the database table: "))
Graph.graphInitialization('C:/Users/Laura/PycharmProjects/TFG/src/SQL/BD.db', tableName)
