"""
This module implements the Interface class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
import os
import subprocess
import sys

from src.final.Estructura import *

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'


class Interface:
    @staticmethod
    def graphOptions(option, graph, rows):
        """
        Create and display different types of graphs: plain, plain with threshold, linear and exponential

        :param option: Option graph
        :param graph: NetworkX's Graph
        :param rows: Rows from a table
        :type option: int
        :type graph: nx.Graph
        """
        if option == 1:
            Graph.createPlainGraph(graph, rows)
            filename = 'plainGraph.dot'
            Graph.exportGraphDOT(graph, filename)
            Interface.openGraphviz(filename)
        elif option == 2:
            Graph.createLinearGraph(graph, rows)
            filename = 'linearGraph.dot'
            Graph.exportGraphDOT(graph, filename)
            Interface.openGraphviz(filename)
        elif option == 3:
            Graph.createExponentialGraph(graph, rows)
            filename = 'exponentialGraph.dot'
            Graph.exportGraphDOT(graph, filename)
            Interface.openGraphviz(filename)
        elif option == 4:
            threshold = int(input("Please enter the k constant for the threshold:\n"))
            Graph.createPlainGraphWithThreshold(graph, rows, threshold)
            filename = 'plainGraphWithThreshold.dot'
            Graph.exportGraphDOT(graph, filename)
            Interface.openGraphviz(filename)

    @staticmethod
    def structureOptions(option, graph, rows):
        """
        Create and display different types of graphs and 2-structures: plain, linear and exponential
        :param option: Option graph
        :param graph: NetworkX's Graph
        :param rows: Rows from a table
        :type option: int
        :type graph: nx.Graph
        """
        if option == 1:
            optionPlain = int(input("Please enter the option of plain graph you want to create:\n [1] = plain\n [2] = "
                                    "plain with threshold\n"))
            if optionPlain == 1:
                plainGraph = Graph.createPlainGraph(graph, rows)
            elif optionPlain == 2:
                threshold = int(input("Please enter the k constant for the threshold:\n"))
                plainGraph = Graph.createPlainGraphWithThreshold(graph, rows, threshold)
            Estructura.plain2structure(plainGraph, plainGraph.nodes())
            Interface.openGraphviz('plain2-structure.dot')
        elif option == 2:
            linearGraph = Graph.createLinearGraph(graph, rows)
            Estructura.linear2structure(linearGraph, linearGraph.nodes())
            Interface.openGraphviz('linear2-structure.dot')
        elif option == 3:
            exponentialGraph = Graph.createExponentialGraph(graph, rows)
            Estructura.exponential2structure(exponentialGraph, exponentialGraph.nodes())
            Interface.openGraphviz('exponential2-structure.dot')

    @staticmethod
    def graphAndstructureOptions(option, graph, rows):
        """
        Create and display different types of 2-structures: plain, linear and exponential

        :param option: Option graph
        :param graph: NetworkX's Graph
        :param rows: Rows from a table
        :type option: int
        :type graph: nx.Graph
        """
        if option == 1:
            optionPlain = int(input("Please enter the option of plain graph you want to create:\n [1] = plain\n [2] = "
                                    "plain with threshold\n"))
            if optionPlain == 1:
                plainGraph = Graph.createPlainGraph(graph, rows)
                filename = 'plainGraph.dot'
                Graph.exportGraphDOT(graph, filename)
                Interface.openGraphviz(filename)
            elif optionPlain == 2:
                threshold = int(input("Please enter the k constant for the threshold:\n"))
                plainGraph = Graph.createPlainGraphWithThreshold(graph, rows, threshold)
                filename = 'plainGraphWithThreshold.dot'
                Graph.exportGraphDOT(graph, filename)
                Interface.openGraphviz(filename)
            Estructura.plain2structure(plainGraph, plainGraph.nodes())
            Interface.openGraphviz('plain2-structure.dot')
        elif option == 2:
            linearGraph = Graph.createLinearGraph(graph, rows)
            filename = 'linearGraph.dot'
            Graph.exportGraphDOT(graph, filename)
            Interface.openGraphviz(filename)
            Estructura.linear2structure(linearGraph, linearGraph.nodes())
            Interface.openGraphviz('linear2-structure.dot')
        elif option == 3:
            exponentialGraph = Graph.createExponentialGraph(graph, rows)
            filename = 'exponentialGraph.dot'
            Graph.exportGraphDOT(graph, filename)
            Interface.openGraphviz(filename)
            Estructura.exponential2structure(exponentialGraph, exponentialGraph.nodes())
            Interface.openGraphviz('exponential2-structure.dot')

    @staticmethod
    def fileOptions(option):
        if option == 1:
            file = str(input("Please enter the name from ARFF data file:\n"))
            # connection, cursor = Data.connection(file[0:-5] + ".db")  # Connection to SQLite database
            connection, cursor = Data.connection("DB" + ".db")  # Connection to SQLite database
            file = Data.openFile(file)  # Open data file
            columnNames, lines = Data.getDataARFFile(file)  # Get column names and lines from file
            tableName = Data.getTableNameFromARFFFile(lines)
            Data.createTableARFF(cursor, tableName, columnNames)  # Create table tableName
            Data.insertARFF(tableName, columnNames, lines, cursor, connection)  # Insert data to tableName
        elif option == 2:
            file = str(input("Please enter the name from DB SQLite file:\n"))
            connection, cursor = Data.connection(file)  # Connection to SQLite database

        return cursor

    @staticmethod
    def openGraphviz(filename):
        """
        Call the Graphviz program that is associated with a DOT file

        :param filename: DOT file
        :type filename: str
        """
        if sys.platform == 'win32':  # Windows platform
            os.startfile(filename)
        else:  # Linux platform
            subprocess.run(['open', '-a', 'Graphviz.app', filename])
