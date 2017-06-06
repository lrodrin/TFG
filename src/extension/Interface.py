"""
This module implements the Interface class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
import subprocess

import six

from src.extension.Structure import *

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'


class Interface:
    @staticmethod
    def inputOptions():
        """
        Manage the input options
        
        """
        s = "Please enter the option for the type of file you provide or Exit:\n [1] = ARFF\n [2] = TXT\n [3] = DB\n " \
            "[0] = Exit\n "
        option = int(six.moves.input(s))
        while option != 0:  # While option is not 0 (Exit option)
            Interface.inputFileOptions(option)  # Manages the data entry
            option = int(six.moves.input(s))

        print("Exit")

    @staticmethod
    def inputFileOptions(option):
        """
        Manages the type of data (ARFF, TXT or DB) entry specified by option

        :param option: Type of data option
        :type option: int
        """
        if option == 1:
            fileARFF = str(six.moves.input("Please enter the name from ARFF file:\n")) + ".arff"
            # connection, cursor = Data.connection(fileARFF[0:-5] + ".arff")  # Connection to SQLite database
            connection, cursor = Data.connectionDB("DB")  # Connection to SQLite database
            file = Data.openFile(fileARFF)  # Open data file
            columnNames, lines = Data.getDataFile(file, "ARFF")  # Get column names and lines from file
            tableName = fileARFF[0:-5]  # Table name
            tables = Data.getTables(cursor)
            if tableName not in tables:  # If tableName not exists
                Data.createTable(cursor, tableName, columnNames)  # Create table specified by tableName
                print("Table %s created" % tableName)
                Data.insertDataARFF(tableName, columnNames, lines, cursor, connection)  # Insert data values to
                # tableName
            else:
                print("Table %s exists" % tableName)

        elif option == 2:
            fileTXT = str(six.moves.input("Please enter the name from TXT file:\n")) + ".txt"
            # connection, cursor = Data.connection(fileTXT[0:-4] + ".txt")  # Connection to SQLite database
            connection, cursor = Data.connectionDB("DB")  # Connection to SQLite database
            file = Data.openFile(fileTXT)  # Open data file
            columnNames, lines = Data.getDataFile(file, "TXT")  # Get column names and lines from file
            tableName = fileTXT[0:-4]  # Table name
            tables = Data.getTables(cursor)
            if tableName not in tables:  # If tableName not exists
                Data.createTable(cursor, tableName, columnNames)  # Create table specified by tableName
                print("Table %s created" % tableName)
                Data.insertDataTXT(tableName, columnNames, lines, cursor, connection)  # Insert data values to
                # tableName

            else:
                print("Table %s exists" % tableName)

        elif option == 3:
            fileDB = str(six.moves.input("Please enter the name from SQLite file:\n")) + ".db"
            # connection, cursor = Data.connection(fileDB[0:-3] + ".db")  # Connection to SQLite database
            connection, cursor = Data.connectionDB("DB")  # Connection to SQLite database
            tableName = fileDB[0:-3]
            tables = Data.getTables(cursor)
            if tableName in tables:  # If tableName exists
                print("Table %s exists" % tableName)

    @staticmethod
    def graphOptions(option, initGraph, rows):
        """
        Manages the creation of graphs (plain, plain with threshold, linear or exponential) specified by option

        :param option: Type of graphs option
        :param initGraph: Initial graph
        :param rows: Rows from a SQLite table
        :type option: str
        :type initGraph: nx.Graph
        :return: A type of graph and the name of graph dot file generated
        :rtype: nx.Graph, str
        """
        s = "Please enter the K constant for the threshold:\n"

        if option == 1:  # Create a plain graph
            graph = Graph.createPlainGraph(initGraph, rows)
            graphName = "plainGraph.dot"

        elif option == 2:  # Create a plain graph with threshold
            threshold = int(six.moves.input(s))
            graph = Graph.createPlainGraphWithThreshold(initGraph, rows, threshold)
            graphName = "plainGraph_with_threshold.dot"

        elif option == 3:  # Create a linear graph
            threshold = int(six.moves.input(s))
            graph = Graph.createLinearGraphWithThreshold(initGraph, rows, threshold)
            graphName = "linearGraph.dot"

        elif option == 4:  # Create an exponential graph
            threshold = int(six.moves.input(s))
            graph = Graph.createExponentialGraphWithThreshold(initGraph, rows, threshold)
            graphName = "exponentialGraph.dot"

        Graph.exportGraph(graph, graphName)  # Export a type of graph to Graphviz format
        print("A graph %s with %d nodes was created" % (graphName, graph.order()))

        return graph, graphName

    @staticmethod
    def structureOptions(option, graph, moreFrequentSubsets):
        """
        Manages the creation of 2-structures (plain, plain with threshold, linear or exponential) specified by option

        :param option: Type of 2-structure option
        :param graph: A graph with the same type 2-structure
        :param moreFrequentSubsets: More frequents nodes from graph
        :type option: str
        :type graph: nx.Graph
        :type moreFrequentSubsets: list
        :return: The name of 2-structure DOT file
        :rtype: str
        """
        if option == 1:  # Create a plain 2-structure
            structureName = "plain_2-structure.dot"
            if moreFrequentSubsets is not None:
                Structure.createFrequent2Structure(graph, structureName, moreFrequentSubsets)
            else:
                Structure.create2Structure(graph, structureName)

        elif option == 2:  # Create a plain 2-structure with threshold
            structureName = "plain_2-structure_with_threshold.dot"
            if moreFrequentSubsets is not None:
                Structure.createFrequent2Structure(graph, structureName, moreFrequentSubsets)
            else:
                Structure.create2Structure(graph, structureName)

        elif option == 3:  # Create a linear 2-structure
            structureName = "linear_2-structure.dot"
            if moreFrequentSubsets is not None:
                Structure.createFrequent2Structure(graph, structureName, moreFrequentSubsets)
            else:
                Structure.create2Structure(graph, structureName)

        elif option == 4:  # Create an exponential 2-structure
            structureName = "exponential_2-structure.dot"
            if moreFrequentSubsets is not None:
                Structure.createFrequent2Structure(graph, structureName, moreFrequentSubsets)
            else:
                Structure.create2Structure(graph, structureName)

        return structureName

    @staticmethod
    def openGraphviz(filename):
        """
        Call the Graphviz program that is associated with a DOT file specified by filename

        :param filename: Dot file
        :type filename: str
        """
        if sys.platform == 'win32':  # Windows platform
            try:
                os.startfile(filename)
            except OSError as e:
                print("Error to open Graphviz program in Windows platform:", e)

        elif sys.platform == 'darwin':  # Mac platform
            try:
                subprocess.call(['open', '-a', 'Graphviz.app', filename])
            except OSError as e:
                print("Error to open Graphviz program in Mac platform:", e)

        elif 'linux' in sys.platform:  # Linux platform
            try:
                os.system("xdot %s" % filename)
            except OSError as e:
                print("Error to open Graphviz program in Linux platform:", e)
