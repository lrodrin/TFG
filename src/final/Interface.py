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
        :param graph: Networkx's Graph
        :param rows: Rows from a SQLite table
        :type option: int
        :type graph: nx.Graph
        """
        if option == 1:
            Graph.createPlainGraph(graph, rows)  # Create a plain graph
            graphName = "plainGraph.dot"
            Graph.exportGraphDOT(graph, graphName)  # Export graph to Graphviz format
        elif option == 2:
            threshold = int(input("Please enter the k constant for the threshold:\n"))
            Graph.createPlainGraphWithThreshold(graph, rows, threshold)  # Create a plain graph with threshold
            graphName = "plainGraphWithThreshold.dot"
            Graph.exportGraphDOT(graph, graphName)  # Export graph to Graphviz format
        elif option == 3:
            Graph.createLinearGraph(graph, rows)  # Create a linear graph
            graphName = "linearGraph.dot"
            Graph.exportGraphDOT(graph, graphName)  # Export graph to Graphviz format
        elif option == 4:
            Graph.createExponentialGraph(graph, rows)  # Create an exponential graph
            graphName = "exponentialGraph.dot"
            Graph.exportGraphDOT(graph, graphName)  # Export graph to Graphviz format

        Interface.openGraphviz(graphName)  # Open graph in Graphviz program

    @staticmethod
    def structureOptions(option, graph, rows):
        """
        Create and display different types of 2-structures: plain, plain with threshold, linear and exponential

        :param option: Option 2-structure
        :param graph: Networkx's Graph
        :param rows: Rows from a SQLite table
        :type option: int
        :type graph: nx.Graph
        """
        if option == 1:
            optionPlain = int(input(
                "Please enter the option of graph you want to create:\n [1] = plain\n [2] = plain with threshold\n"))
            if optionPlain == 1:
                structureName = "plain 2-structure.dot"
                plainGraph = Graph.createPlainGraph(graph, rows)  # Create a plain graph
            elif optionPlain == 2:
                structureName = "plain 2-structure with threshold.dot"
                threshold = int(input("Please enter the k constant for the threshold:\n"))
                plainGraph = Graph.createPlainGraphWithThreshold(graph, rows,
                                                                 threshold)  # Create a plain graph with threshold

            Estructura.plain2structure(plainGraph, plainGraph.nodes(), structureName)  # Create a plain 2-structure

        elif option == 2:
            structureName = "linear 2-structure.dot"
            linearGraph = Graph.createLinearGraph(graph, rows)
            Estructura.linear2structure(linearGraph, linearGraph.nodes(), structureName)  # Create a linear 2-structure
        elif option == 3:
            structureName = "exponential 2-structure.dot"
            exponentialGraph = Graph.createExponentialGraph(graph, rows)
            Estructura.exponential2structure(exponentialGraph, exponentialGraph.nodes(),
                                             structureName)  # Create an exponential 2-structure

        Interface.openGraphviz(structureName)  # Open 2-structure in Graphviz program

    @staticmethod
    def graphANDstructureOptions(option, graph, rows):
        """
        Create and display different types of graph and 2-structures: plain, plain with threshold, linear and exponential

        :param option: Option graph and 2-structure
        :param graph: Networkx's Graph
        :param rows: Rows from a SQLite table
        :type option: int
        :type graph: nx.Graph
        """
        if option == 1:
            optionPlain = int(input(
                "Please enter the option of graph you want to create:\n [1] = plain\n [2] = plain with threshold\n"))
            if optionPlain == 1:
                graphName = "plainGraph.dot"
                structureName = "plain 2-structure.dot"
                plainGraph = Graph.createPlainGraph(graph, rows)  # Create a plain graph
                Graph.exportGraphDOT(graph, graphName)  # Export graph to Graphviz format
                Estructura.plain2structure(plainGraph, plainGraph.nodes(), structureName)  # Create a plain 2-structure
            elif optionPlain == 2:
                graphName = "plainGraph with threshold.dot"
                structureName = "plain 2-structure with threshold.dot"
                threshold = int(input("Please enter the k constant for the threshold:\n"))
                plainGraph = Graph.createPlainGraphWithThreshold(graph, rows, threshold)  # Create a plain graph with
                #  threshold
                Graph.exportGraphDOT(graph, graphName)  # Export graph to Graphviz format
                Estructura.plain2structure(plainGraph, plainGraph.nodes(), structureName)  # Create a plain 2-structure

        elif option == 2:
            graphName = "linearGraph.dot"
            structureName = "linear 2-structure.dot"
            linearGraph = Graph.createLinearGraph(graph, rows)  # Create a linear graph
            Graph.exportGraphDOT(graph, graphName)  # Export graph to Graphviz format
            Estructura.linear2structure(linearGraph, linearGraph.nodes(), structureName)
        elif option == 3:
            graphName = "exponentialGraph.dot"
            structureName = "exponential 2-structure.dot"
            exponentialGraph = Graph.createExponentialGraph(graph, rows)  # Create an exponential graph
            Graph.exportGraphDOT(graph, graphName)  # Export graph to Graphviz format
            Estructura.exponential2structure(exponentialGraph, exponentialGraph.nodes(), structureName)

        Interface.openGraphviz(graphName)   # Open graph in Graphviz program
        Interface.openGraphviz(structureName)  # Open 2-structure in Graphviz program

    @staticmethod
    def fileOptions(option):
        if option == 1:
            file = str(input("Please enter the name from arff file:\n"))
            connection, cursor = Data.connection(file[0:-5] + ".db")  # Connection to SQLite database
            file = Data.openFile(file)  # Open data file
            columnNames, lines = Data.getDataARFFile(file)  # Get column names and lines from data file
            tableName = Data.getTableNameFromARFFFile(lines)  # Get table name from data file
            Data.createTableARFF(cursor, tableName, columnNames)  # Create table tableName
            Data.insertARFF(tableName, columnNames, lines, cursor, connection)  # Insert data values to tableName

        elif option == 2:
            file = str(input("Please enter the name from SQLite file:\n"))
            connection, cursor = Data.connection(file)  # Connection to SQLite database

        return cursor

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
            subprocess.run(['open', '-a', 'Graphviz.app', filename])
