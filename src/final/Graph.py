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
    def graphInitialization(fileDB, tableName):
        """
        Create and initializes a Graph from SQLite database source

        :param fileDB: SQLite database file
        :param tableName: Table name from fileDB
        """
        graph = nx.Graph()
        connection = Data.connection(fileDB)  # Connection to SQLite database
        cursor = connection.cursor()
        # TODO tableName = Data.getTableName(fileDB)
        columnNames, rows = Data.select(tableName, cursor)  # Select data from SQLite database
        Graph.addNodes(nx.Graph(), columnNames, rows)  # Adding nodes to a Graph
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
    def createPlanarGraph(graph, rows):
        for row in rows:
            for (u, v) in itertools.combinations(row, 2):
                graph.add_edge(u, v, color='black')
        return graph, Graph.exportGraphDOT(graph, 'planarGraph.dot')

    @staticmethod
    def linearGraph(graph, rows):
        # labeling edges
        d = dict()
        for row in rows:
            for (u, v) in itertools.combinations(row, 2):
                if (u, v) in d.keys():
                    d[(u, v)] = d.get((u, v)) + 1
                    graph.edge[u][v]['label'] += 1
                else:
                    d[(u, v)] = 1
                    graph.edge[u][v]['label'] = 1

        # painting edges by label
        colors = {0: 'white', 1: 'black', 2: 'cyan', 3: 'green', 4: 'magenta', 5: 'orange', 6: 'purple', 7: 'red',
                  8: 'yellow',
                  9: 'brown'}
        for key, value in colors.items():
            for u, v in graph.edges():
                if 'label' in graph[u][v] and key == graph[u][v]['label']:
                    graph[u][v]['color'] = value

        # TODO s'han d'amagar els labels
        return graph, Graph.exportGraphDOT(graph, 'linearGraph.dot')

    @staticmethod
    def exponentialGraph(graph, rows):
        pass
