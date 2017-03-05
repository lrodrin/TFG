"""
This module implements a Gaifman graph from database and create a 2-structure of this graph

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
import sqlite3
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
    connection = sqlite3.connect('C:/Users/Laura/PycharmProjects/TFG/src/SQL/BD.db')  # WINDOWS
    # connection = sqlite3.connect('/Users/laura/PycharmProjects/TFG/src/SQL/BD.db')    # OS X
except sqlite3.Error as e:
    print("Error:", e)

cur = connection.cursor()

try:
    file = open('C:/Users/Laura/PycharmProjects/TFG/src/SQL/meteo.txt', 'r')  # WINDOWS
    # file = open('/Users/laura/PycharmProjects/TFG/src/SQL/meteo.txt', 'r')  # OS X
except IOError as e:
    print("Error:", e)

# lines = file.readlines()  # Keep all lines from data file into lines
# header = lines[0]  # Extract the header from lines
# for word in header.split(" "):  # For each word from header
#     colNames += word + ", "  # Adding a column into colNames

tableName = str(input("Please enter a name for the database table: "))
# try:
#     query = "CREATE TABLE %s (%s);" % (str(tableName), str(colNames[0:-2]))  # Create a table
#     cur.execute(query)
#     print("Created table %s..." % tableName)
# except sqlite3.Error as e:
#     print("Error:", e)

# for i in range(1, len(lines)):  # For each row from data file
#     for col in lines[i].split(" "):  # For each column in lines[i]
#         values += "'%s'," % col.split(":")[1]  # Extract and save the value
#     try:
#         query = 'INSERT INTO {0} ({1}) VALUES ({2});'.format(str(tableName), str(colNames[0:-2]),
#                                                              str(values[0:-1]).replace('\n', ''))
#
#         # Insert values to table
#         cur.execute(query)
#         connection.commit()
#         print("Inserted row number %d" % i)
#     except sqlite3.Error as e:
#         print("Error:", e)
#     values = ""

cur.execute("SELECT * FROM %s" % tableName)
colNames = [description[0] for description in cur.description]
rows = cur.fetchall()

graph = g.Graph.G
# add nodes
g.Graph.addNodes(graph, colNames, rows)
# initialization of edges
g.Graph.initialization(graph)

# planar graph
planarGraph, planarDOT = g.Graph.planarGraph(graph, rows)
# linear graph
linearGraph, linearDOT = g.Graph.linearGraph(graph, rows)
# exponential graph
# exponentialGraph, exponentialDOT = g.Graph.exponentialGraph(graph, rows)

# planar structure
e.Estructura.planarStructure(planarGraph, set(planarGraph.nodes()))
# linear structure
# exponential structure

e.Estructura.openGraphviz('', 'planar-structure.dot')  # WINDOWS
file.close()
cur.close()
connection.close()
