"""
This module implements the Graph class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
import itertools

import networkx as nx

from src.final.Data import *

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'


# TODO Linies discontinues enlloc del color blanc

class Graph:
    @staticmethod
    def initGraph(tableName, cursor):
        """
        Create and initializes a graph from SQLite database source

        :param tableName: Table name
        :param cursor: Cursor object
        :type tableName: str
        :return: A graph and all rows from tableName
        :rtype: nx.Graph
        """
        graph = nx.Graph()
        columnNames, rows = Data.select(tableName, cursor)  # Select data from tableName
        Graph.addNodes(graph, columnNames, rows)  # Adding nodes to graph
        for (u, v) in itertools.combinations(graph.nodes(), 2):  # For initialization all the edges from graph are
            # painted white
            graph.add_edge(u, v, color='white')

        return graph, rows

    @staticmethod
    def exportGraph(graph, filename):
        """
        Export a graph to Graphviz Dot format

        :param graph: Networkx's graph
        :param filename: File name
        :type graph: nx.Graph
        :type filename: str
        """
        nx.nx_pydot.write_dot(graph, filename)

    @staticmethod
    def getAttributesFromGraph(graph):
        """
        Return a dictionary of attributes from graph keyed by edge

        :param graph: Networkx's graph
        :type graph: nx.Graph
        :return A dictionary of attributes from graph
        :rtype: dict
        """
        graphDict = nx.get_edge_attributes(graph, 'color')
        return graphDict

    @staticmethod
    def addNodes(graph, columnNames, rows):
        """
        Add nodes to graph through SQLite database data source

        :param graph: Networkx's graph
        :param columnNames: Column names from a SQLite table
        :param rows: Rows from a SQLite table
        :type graph: nx.Graph
        :type columnNames: str
        """
        for i in range(0, len(columnNames)):  # For each column from a SQLite table
            for row in rows:  # For each row from a SQLite table
                graph.add_node(row[i])  # Add node to graph

    @staticmethod
    def createPlainGraph(graph, rows):
        """
        Create a plain graph from a SQLite rows specified by rows

        :param graph: Networkx's graph
        :param rows: Rows from a SQLite table
        :type graph: nx.Graph
        :return: A plain graph
        :rtype: nx.Graph
        """
        for row in rows:  # For each row in rows
            for (u, v) in itertools.combinations(row, 2):  # For each pair of rows
                if graph.has_edge(u, v):  # If exists edge (u, v) in graph
                    graph.edge[u][v]['color'] = 'black'  # Edge painted black
        return graph

    @staticmethod
    def createPlainGraphWithThreshold(graph, rows, k):
        """
        Create a plain graph from a SQLite rows specified by rows

        :param graph: Networkx's graph
        :param rows: Rows from a SQLite table
        :param k: Threshold
        :type graph: nx.Graph
        :type k: int
        :return: A Plain graph with threshold
        :rtype: nx.Graph
        """
        Graph.labelEdges(graph, rows)  # labeling edges
        # painting edges by label
        labels = nx.get_edge_attributes(graph, 'label')  # Labels from graph
        for (u, v), label in labels.items():  # For each label in graph
            if label < k:  # If label is smaller than k constant
                graph[u][v]['color'] = 'white'  # Edge white
            else:  # If label is equal or greater than k constant
                graph[u][v]['color'] = 'black'  # Edge painted black

        return graph

    @staticmethod
    def labelEdges(graph, rows):
        """
        Count the number of equivalences and label the edges from graph with this number

        :param graph: Networkx's graph
        :param rows: Rows from a SQLite table
        :type graph: nx.Graph
        """
        dictionary = dict()
        for row in rows:  # For each row in rows
            for (u, v) in itertools.combinations(row, 2):  # For each pair of rows
                if (u, v) in dictionary.keys():  # If exists edge (u, v) in dictionary
                    dictionary[(u, v)] = dictionary.get((u, v)) + 1
                    graph.edge[u][v]['label'] += 1  # Add 1 to the label that counts the (u, v) occurrences in
                    # dictionary

                else:  # If not exists edge (u, v) in dictionary, initializes the label 1
                    dictionary[(u, v)] = 1
                    graph.add_edge(u, v, label=1)

    @staticmethod
    def createLinearGraph(graph, rows):
        """
        Create a linear graph from a SQLite rows specified by rows

        :param graph: Networkx's graph
        :param rows: Rows from a SQLite table
        :type graph: nx.Graph
        :return: A linear graph
        :rtype: nx.Graph
        """
        Graph.labelEdges(graph, rows)  # labeling edges
        # painting edges by label
        colors = {0: 'white', 1: 'black', 2: 'cyan', 3: 'green', 4: 'magenta', 5: 'orange', 6: 'purple', 7: 'red',
                  8: 'yellow', 9: 'brown'}  # Dictionary of possible labels and colours
        for label, color in colors.items():  # For each label and color
            for (u, v) in graph.edges():  # For each pair of nodes from graph
                if 'label' in graph[u][v] and label == graph[u][v]['label']:  # If label is labeled in graph and
                    # label is the edge label
                    graph[u][v]['color'] = color  # Add color to edge

        return graph

    @staticmethod
    def createExponentialGraph(linearGraph, rows):
        """
        Create a exponential graph from a SQLite rows specified by rows

        :param linearGraph: Networkx's graph
        :param rows: Rows from a SQLite table
        :type linearGraph: nx.Graph
        :return: An exponential graph
        :rtype: nx.Graph
        """
        graph = Graph.createLinearGraph(linearGraph, rows)  # Create a linear graph
        labels = nx.get_edge_attributes(graph, 'label')
        # painting edges by label
        for (u, v), label in labels.items():  # For each label
            if 0 <= label < 1:
                graph[u][v]['color'] = 'white'
            elif 1 <= label < 2:
                graph[u][v]['color'] = 'black'
            elif 2 <= label < 4:
                graph[u][v]['color'] = 'cyan'
            elif 4 <= label < 8:
                graph[u][v]['color'] = 'green'
            elif 8 <= label < 16:
                graph[u][v]['color'] = 'magenta'
            elif 16 <= label < 32:
                graph[u][v]['color'] = 'orange'
            elif 32 <= label < 64:
                graph[u][v]['color'] = 'purple'
            elif 64 <= label < 128:
                graph[u][v]['color'] = 'red'
            elif 128 <= label < 256:
                graph[u][v]['color'] = 'yellow'
            else:
                graph[u][v]['color'] = 'brown'

        return graph

    @staticmethod
    def graphOptions(option, initGraph, rows):
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
        print("%s was created" % graphName)

        return graph
