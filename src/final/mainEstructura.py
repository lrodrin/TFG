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
    # primalsList_1 = [frozenset({'B'}), frozenset({'A'}), frozenset({'D'}), frozenset({'C'}), frozenset({'E'}),
    #                  frozenset({'E', 'D'}), frozenset({'A', 'E', 'D'}), frozenset({'A', 'E', 'D', 'B'}),
    #                  frozenset({'A', 'E', 'D', 'C', 'B'})]
    # primalsList_2 = [frozenset({'C'}), frozenset({'A'}), frozenset({'D'}), frozenset({'F'}), frozenset({'E'}),
    #                  frozenset({'B'}), frozenset({'D', 'C'}), frozenset({'B', 'A'}),
    #                  frozenset({'D', 'B', 'E', 'F', 'C', 'A'})]
    #
    # edgesAtributtesfromGraph_1 = {('C', 'B'): 'black', ('B', 'A'): 'red', ('D', 'A'): 'blue', ('E', 'A'): 'blue',
    #                               ('C', 'A'): 'black', ('E', 'C'): 'black', ('D', 'B'): 'red', ('E', 'B'): 'red',
    #                               ('E', 'D'): 'red', ('C', 'D'): 'black'}
    # edgesAtributtesfromGraph_2 = {('D', 'C'): 'red', ('B', 'C'): 'black', ('F', 'C'): 'blue', ('D', 'A'): 'black',
    #                               ('E', 'A'): 'black', ('B', 'A'): 'black', ('D', 'B'): 'black', ('B', 'E'): 'black',
    #                               ('A', 'C'): 'black', ('E', 'C'): 'orange', ('D', 'E'): 'orange', ('D', 'F'): 'blue',
    #                               ('A', 'F'): 'green', ('E', 'F'): 'red', ('B', 'F'): 'green'}
    #
    # primalsDict_1 = OrderedDict(reversed(sorted(Clan.primalClansDict(primalsList_1).items(),
    #                                             key=lambda t: len(t[0]))))
    # primalsDict_2 = OrderedDict(reversed(sorted(Clan.primalClansDict(primalsList_2).items(),
    #                                             key=lambda t: len(t[0]))))
    #
    # print("First primals list:\n", primalsDict_1)
    # print("Second primals list:\n", primalsDict_2)
    #
    # Estructura.create2structure(edgesAtributtesfromGraph_1, primalsDict_1, 'Estructura.dot')
    # Estructura.create2structure(edgesAtributtesfromGraph_2, primalsDict_2, 'Estructura2.dot')

    fileOption = int(input("Please enter the option for the file you provide:\n [1] = .arff\n [2] = .db\n"))
    if fileOption == 1:
        file = str(input("Please enter the name from ARFF data file:\n"))
        # connection, cursor = Data.connection(file[0:-5] + ".db")  # Connection to SQLite database
        # connection, cursor = Data.connection("DB" + ".db")  # Connection to SQLite database
        # file = Data.openFile(file)  # Open data file
        # columnNames, lines = Data.getDataARFFile(file)  # Get column names and lines from file
        # tableName = Data.getTableNameARFF(lines)
        # Data.createTableARFF(cursor, tableName, columnNames)  # Create table tableName
        # Data.insertARFF(tableName, columnNames, lines, cursor, connection)  # Insert data to tableName
    elif fileOption == 2:
        file = str(input("Please enter the name from DB SQLite file:\n"))
        connection, cursor = Data.connection(file)  # Connection to SQLite database

    tableName = str(input("Table name: \n"))
    graph, rows = Graph.initializeGraph(tableName, cursor)

    option = int(input("Please enter the option of 2-structure you want to create:\n [1] = plain\n [2] = linear\n [3] "
                       "= exponential\n"))
    if option == 1:
        optionPlain = int(input("Please enter the option of plain graph you want to create:\n [1] = plain\n [2] = "
                                "plain with threshold\n"))
        if optionPlain == 1:
            plainGraph = Graph.createPlainGraph(graph, rows)
        elif optionPlain == 2:
            threshold = int(input("Please enter the k constant for the threshold:\n"))
            plainGraph = Graph.createPlainGraphWithThreshold(graph, rows, threshold)
        Estructura.plain2structure(plainGraph, plainGraph.nodes())
    elif option == 2:
        linearGraph = Graph.createLinearGraph(graph, rows)
        Estructura.linear2structure(linearGraph, linearGraph.nodes())
    elif option == 3:
        exponentialGraph = Graph.createExponentialGraph(graph, rows)
        Estructura.exponential2structure(exponentialGraph, exponentialGraph.nodes())
