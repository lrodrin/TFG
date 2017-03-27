"""
This module implements the Interface class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
import os
import subprocess
import sys

import six

from src.final.Structure import *

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'


class Interface:
    @staticmethod
    def inputFileOptions(option):
        """
        Manages the type of data (ARFF, TXT or DB) entry specified by option

        :param option: Type of data option
        :type option: str
        :return: The column names, rows, cursor and tableName generated for one type of data
        """
        if option == 1:
            fileARFF = str(six.moves.input("Please enter the name from ARFF file:\n")) + ".arff"
            # connection, cursor = Data.connection(fileARFF[0:-5] + ".arff")  # Connection to SQLite database
            connection, cursor = Data.connection("DB")  # Connection to SQLite database
            file = Data.openFile(fileARFF)  # Open data file
            columnNames, lines = Data.getDataFile(file, "ARFF")  # Get column names and lines from data file
            tableName = Data.getNameForTableNameFromARFF(lines)  # Get table name from data file
            Data.createTable(cursor, tableName, columnNames)  # Create table tableName
            Data.insertARFF(tableName, columnNames, lines, cursor, connection)  # Insert data values to tableName
            columnNames, rows = Data.select(tableName, cursor)  # Select data from tableName

        elif option == 2:
            fileTXT = str(six.moves.input("Please enter the name from TXT file:\n")) + ".txt"
            # connection, cursor = Data.connection(fileTXT[0:-4] + ".txt")  # Connection to SQLite database
            connection, cursor = Data.connection("DB")  # Connection to SQLite database
            file = Data.openFile(fileTXT)  # Open data file
            columnNames, lines = Data.getDataFile(file, "TXT")  # Get column names and lines from file
            tableName = str(
                six.moves.input("Please enter the table name which to create the new SQLite table from file: \n"))
            Data.createTable(cursor, tableName, columnNames)  # Create table tableName
            Data.insertTXT(tableName, columnNames, lines, cursor, connection)  # Insert data values to tableName
            columnNames, rows = Data.select(tableName, cursor)  # Select data from tableName

        elif option == 3:
            # fileDB = str(six.moves.input("Please enter the name from SQLite file:\n")) + ".db"
            # connection, cursor = Data.connection(fileDB[0:-3] + ".db")  # Connection to SQLite database
            connection, cursor = Data.connection("DB")  # Connection to SQLite database
            tableName = str(
                six.moves.input("Please enter the table name which to select from SQLite database: \n"))
            columnNames, rows = Data.select(tableName, cursor)  # Select data from tableName

        return columnNames, rows, cursor, tableName

    @staticmethod
    def graphOptions(option, initGraph, rows):
        """
        Manages the creation of graphs (plain, plain with threshold, linear or exponential) specified by option

        :param option: Type of graphs option
        :param initGraph: Initial graph
        :param rows: Rows from a SQLite table
        :type option: str
        :type initGraph: nx.Graph
        :return: A type of graph and the name of graph dot file
        :rtype: nx.Graph, str
        """
        if option == 1:
            graph = Graph.createPlainGraph(initGraph, rows)  # Create a plain graph
            graphName = "plainGraph.dot"

        elif option == 2:
            threshold = int(six.moves.input("Please enter the K constant for the threshold:\n"))
            graph = Graph.createPlainGraphWithThreshold(initGraph, rows,
                                                        threshold)  # Create a plain graph with threshold
            graphName = "plainGraph with threshold.dot"

        elif option == 3:
            graph = Graph.createLinearGraph(initGraph, rows)  # Create a linear graph
            graphName = "linearGraph.dot"

        elif option == 4:
            graph = Graph.createExponentialGraph(initGraph, rows)  # Create an exponential graph
            graphName = "exponentialGraph.dot"

        Graph.exportGraph(graph, graphName)  # Export a type of graph to Graphviz format
        print("A graph %s was created" % graphName)

        return graph, graphName

    @staticmethod
    def structureOptions(option, graph):
        """
        Manages the creation of 2-structures (plain, plain with threshold, linear or exponential) specified by option

        :param option: Type of 2-structure option
        :param graph: A graph of the same type 2-structure
        :type option: str
        :type graph: nx.Graph
        :return: The name of 2-structure dot file
        :rtype: str
        """
        if option == 1:
            structureName = "plain 2-structure.dot"
            Structure.create2Structure(graph, graph.nodes(), structureName)  # Create a plain 2-structure

        elif option == 2:
            structureName = "plain 2-structure with threshold.dot"
            Structure.create2Structure(graph, graph.nodes(), structureName)  # Create a plain 2-structure with
            # threshold

        elif option == 3:
            structureName = "linear 2-structure.dot"
            Structure.create2Structure(graph, graph.nodes(), structureName)  # Create a linear 2-structure

        elif option == 4:
            structureName = "exponential 2-structure.dot"
            Structure.create2Structure(graph, graph.nodes(), structureName)  # Create an exponential 2-structure

        return structureName

    @staticmethod
    def openGraphviz(filename):
        """
        Call the Graphviz program that is associated with a Dot file specified by filename

        :param filename: Dot file
        :type filename: str
        """
        if sys.platform == 'win32':  # Windows platform
            os.startfile(filename)
        else:  # Linux platform
            subprocess.call(['open', '-a', 'Graphviz.app', filename])
