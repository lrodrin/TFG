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


class Graph:
    @staticmethod
    def createGraph(fileDB, tableName):
        """
        Create and initializes a Graph from SQLite database source

        :param fileDB: SQLite database file
        :param tableName: Table name from fileDB
        :return: Graph and all rows from from SQLite database source
        :rtype: nx.Graph
        """
        graph = nx.Graph()
        connection = Data.connection(fileDB)  # Connection to SQLite database
        cursor = connection.cursor()
        # TODO tableName = Data.getTableName(fileDB)
        columnNames, rows = Data.select(tableName, cursor)  # Select data from SQLite database
        Graph.addNodes(graph, columnNames, rows)  # Adding nodes to a Graph
        for (u, v) in itertools.combinations(graph.nodes(), 2):  # All the edges are painted white
            graph.add_edge(u, v, color='white')

        return graph, rows

    @staticmethod
    def exportGraphDOT(graph, filename):
        """
        Export graph to Graphviz DOT format

        :param graph: NetworkX's graph
        :param filename: File name for a DOT file
        :type graph: nx.Graph
        :type filename: str
        :return: Graph to Graphviz DOT format
        :rtype: DOT file
        """
        nx.nx_pydot.write_dot(graph, filename)

    @staticmethod
    def createDictFromGraph(graph):
        """
        Return a dictionary of attributes keyed by edge from graph

        :param graph: NetworkX's graph
        :type graph: nx.Graph
        :return graphDict
        :rtype: dict
        """
        graphDict = nx.get_edge_attributes(graph, 'color')
        return graphDict

    @staticmethod
    def addNodes(graph, columnNames, rows):
        """
        Add nodes to graph through SQLite database data source

        :param graph: NetworkX's graph
        :param columnNames: Column names from tableName
        :param rows: Rows from tableName
        :type graph: nx.Graph
        """
        for i in range(0, len(columnNames)):  # For each column from tableName
            for row in rows:  # For each row from tableName
                graph.add_node(row[i])  # Add node to graph

    @staticmethod
    def createPlainGraph(graph, rows):
        """
        Create a plain graph from rows

        :param graph: NetworkX's graph
        :param rows: Rows from a tableName
        :type graph: nx.Graph
        :return: Plain graph
        :rtype: nx.Graph
        """
        for row in rows:
            for (u, v) in itertools.combinations(row, 2):
                graph.add_edge(u, v, color='black')
        return graph

    @staticmethod
    def createLinearGraph(graph, rows):
        """
        Create a linear graph from rows

        :param graph: NetworkX's graph
        :param rows: Rows from a tableName
        :type graph: nx.Graph
        :return: Linear graph
        :rtype: nx.Graph
        """
        # labeling edges
        d = dict()
        for row in rows:
            for (u, v) in itertools.combinations(row, 2):
                if (u, v) in d.keys():
                    d[(u, v)] = d.get((u, v)) + 1
                    graph.edge[u][v]['label'] += 1
                else:
                    d[(u, v)] = 1
                    graph.add_edge(u, v, label=1)

        # painting edges by label
        colors = {0: 'white', 1: 'black', 2: 'cyan', 3: 'green', 4: 'magenta', 5: 'orange', 6: 'purple', 7: 'red',
                  8: 'yellow', 9: 'brown'}
        for key, value in colors.items():
            for u, v in graph.edges():
                if 'label' in graph[u][v] and key == graph[u][v]['label']:
                    graph[u][v]['color'] = value

        # TODO s'han d'amagar els labels
        return graph

    @staticmethod
    def createExponentialGraph(linearGraph, rows):
        """
        Create a exponential graph starting from linear graph

        :param linearGraph: NetworkX's graph
        :param rows: Rows from a tableName
        :type linearGraph: nx.Graph
        :return: Linear graph
        :rtype: nx.Graph
        """
        # painting edges by label
        graph = Graph.createLinearGraph(linearGraph, rows)
        labels = nx.get_edge_attributes(graph, 'label')
        for (u, v), label in labels.items():
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

        # TODO s'han d'amagar els labels
        return graph
