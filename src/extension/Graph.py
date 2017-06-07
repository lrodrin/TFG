"""
This module implements the Graph class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
from itertools import combinations

import networkx as nx

from src.extension.Data import *

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'


class Graph:
    # @staticmethod
    # def initGraph(tableName, cursor):
    #     """
    #     Create and initializes a graph from a table SQLite database source
    #
    #     :param tableName: Table name
    #     :param cursor: Cursor object
    #     :type tableName: str
    #     :return: A graph
    #     :rtype: nx.Graph
    #     """
    #     graph = nx.Graph()  # Create an empty graph with no nodes and no edges
    #     columnNames, rows = Data.selectData(tableName, cursor)  # Select data from tableName
    #     Graph.addNodes(graph, columnNames, rows)  # Adding nodes to graph
    #     for (u, v) in combinations(graph.nodes(), 2):  # For the initialization all the edges from graph are
    #         # painted black and the edge style is dashed
    #         if u != v: # If u and v have different values
    #             graph.add_edge(u, v, color='black', style='dashed')
    #
    #     return graph, rows

    @staticmethod
    def initGraph(tableNames, cursor):
        """
        Create and initializes a graph from different tables SQLite database source

        :param tableNames: Table names
        :param cursor: Cursor object
        :type tableNames: list
        :return: A graph
        :rtype: nx.Graph
        """
        graph = nx.Graph()  # Create an empty graph with no nodes and no edges
        for tableName in tableNames:  # For each tableName in tableNames
            columnNames, rows = Data.selectData(tableName, cursor)  # Select data from tableName
            Graph.addNodes(graph, columnNames, rows)  # Adding nodes to graph
            for (u, v) in combinations(graph.nodes(), 2):  # For the initialization all the edges from graph are
                # painted black and the edge style is dashed
                if u != v:  # If u and v have different values
                    graph.add_edge(u, v, color='black', style='dashed')

        return graph

    @staticmethod
    def addNodes(graph, columnNames, rows):
        """
        Add nodes to graph

        :param graph: Networkx's graph
        :param columnNames: Column names from a SQLite table
        :param rows: Rows from a SQLite table
        :type graph: nx.Graph
        :type columnNames: str
        """
        for i in range(0, len(columnNames)):  # For each column from a SQLite table
            for row in rows:  # For each row from a SQLite table
                if not graph.add_node(row[i]):  # If not exists node(row[i])
                    graph.add_node(row[i])  # Add node to graph

    @staticmethod
    def getColorAttributesFromGraph(graph):
        """
        Return a dictionary of color edges attributes from graph

        :param graph: Networkx's graph
        :type graph: nx.Graph
        :return Color edge's attributes from graph
        :rtype: dict
        """
        graphDict = nx.get_edge_attributes(graph, 'color')
        return graphDict

    @staticmethod
    def getLabelAttributesFromGraph(graph):
        """
        Return a dictionary of label edges attributes from graph

        :param graph: Networkx's graph
        :type graph: nx.Graph
        :return Label edge's attributes from graph
        :rtype: dict
        """
        graphDict = nx.get_edge_attributes(graph, 'label')
        return graphDict

    @staticmethod
    def getStyleAttributesFromGraph(graph):
        """
        Return a dictionary of style edges attributes from graph

        :param graph: Networkx's graph
        :type graph: nx.Graph
        :return Style edge's attributes from graph
        :rtype: dict
        """
        graphDict = nx.get_edge_attributes(graph, 'style')
        return graphDict

    @staticmethod
    def labeledEdges(graph, rowsList):
        """
        Count the number of equivalences and label the edges from graph with the total number of equivalences

        :param graph: Networkx's graph
        :param rowsList: Rows from SQLite tables
        :type graph: nx.Graph
        :type rowsList: list
        """
        # numberOfEquivalences = dict()
        # for row in rows:  # For each row in rows
        #     for (u, v) in combinations(row, 2):  # For each pair (u, v) in the row
        #         if u != v:  # If u and v have different values
        #             if (u, v) in numberOfEquivalences.keys():  # If exists edge (u, v) in a numberOfEquivalences
        #                 numberOfEquivalences[(u, v)] = numberOfEquivalences.get(
        #                     (u, v)) + 1  # Increases the number of equivalences
        #                 graph.edge[u][v]['label'] += 1  # Add the number of equivalences into label edge from graph
        #
        #             else:  # If not exists edge (u, v) in numberOfEquivalences
        #                 numberOfEquivalences[(u, v)] = 1
        #                 graph.add_edge(u, v, label=1)
        numberOfEquivalences = dict()
        for rows in rowsList:  # For each rows in rowsList
            for row in rows:  # For each row in rows
                for (u, v) in combinations(row, 2):  # For each pair (u, v) in the row
                    if u != v:  # If u and v have different values
                        if (u, v) in numberOfEquivalences.keys():  # If exists edge (u, v) in a numberOfEquivalences
                            numberOfEquivalences[(u, v)] = numberOfEquivalences.get(
                                (u, v)) + 1  # Increases the number of equivalences
                            graph.edge[u][v]['label'] += 1  # Add the number of equivalences into label edge from graph

                        else:  # If not exists edge (u, v) in numberOfEquivalences
                            numberOfEquivalences[(u, v)] = 1
                            graph.add_edge(u, v, label=1)

    @staticmethod
    def createPlainGraph(graph, rows):
        """
        Create a plain graph

        :param graph: Networkx's graph
        :param rows: Rows from a SQLite table
        :type graph: nx.Graph
        :return: A plain graph
        :rtype: nx.Graph
        """
        Graph.labeledEdges(graph, rows)  # Labeling edges from graph
        labels = Graph.getLabelAttributesFromGraph(graph)  # Edge labels from graph
        nodesDisconnectedList = graph.nodes().copy()  # List copied of nodesList

        for (u, v), label in labels.items():  # For each edge and label attribute in labels
            if graph.has_edge(u, v) and u != v:  # If exists edge (u, v) in graph and u and v have different values
                if label >= 1:  # If label attribute from edge(u, v) is bigger than 0
                    graph.add_edge(u, v, color='black', style='solid')  # Edge painted black and line style is not
                    # dashed
                    if u in nodesDisconnectedList:
                        nodesDisconnectedList.remove(u)
                    if v in nodesDisconnectedList:
                        nodesDisconnectedList.remove(v)
                # else:
                    # graph.remove_edge(u, v)

        diff = list(set(nodesDisconnectedList) - set(nodesDisconnectedList[0]))
        graph.remove_nodes_from(diff)
        mapping = {nodesDisconnectedList[0]: 'Others'}
        newGraph = nx.relabel_nodes(graph, mapping)

        return newGraph

    @staticmethod
    def createPlainGraphWithThreshold(graph, rows, k):
        """
        Create a plain graph with threshold

        :param graph: Networkx's graph
        :param rows: Rows from a SQLite table
        :param k: Threshold
        :type graph: nx.Graph
        :type k: int
        :return: A plain graph with threshold
        :rtype: nx.Graph
        """
        Graph.labeledEdges(graph, rows)  # Labeling edges from graph
        labels = Graph.getLabelAttributesFromGraph(graph)  # Edge labels from graph
        nodesDisconnectedList = graph.nodes().copy()  # List copied of nodesList
        newGraph = nx.Graph()
        print(nodesDisconnectedList)

        for (u, v), label in labels.items():  # For each edge and label attribute in labels
            if graph.has_edge(u, v) and u != v:  # If exists edge (u, v) in graph and u and v have different values
                if label >= k:  # If label attribute from edge(u, v) is bigger than k
                    graph.add_edge(u, v, color='black', style='solid')  # Edge painted black and line style is not
                    # dashed
                    if u in nodesDisconnectedList:
                        nodesDisconnectedList.remove(u)
                    if v in nodesDisconnectedList:
                        nodesDisconnectedList.remove(v)

        if len(nodesDisconnectedList) != 0:
            diff = list(set(nodesDisconnectedList[0]) - set(nodesDisconnectedList))
            print(diff)
            graph.remove_nodes_from(diff)
            print(nodesDisconnectedList[0])
            mapping = {nodesDisconnectedList[0]: 'Others'}
            newGraph = nx.relabel_nodes(graph, mapping)

        else:
            newGraph = graph

        print(newGraph.nodes(), nodesDisconnectedList)

        return newGraph

    @staticmethod
    def createLinearGraph(graph, rows):
        """
        Create a linear graph

        :param graph: Networkx's graph
        :param rows: Rows from a SQLite table
        :type graph: nx.Graph
        :return: A linear graph
        :rtype: nx.Graph
        """
        Graph.labeledEdges(graph, rows)  # Labeling edges from graph
        labels = Graph.getLabelAttributesFromGraph(graph)  # Edge labels from graph

        for (u, v), label in labels.items():  # For each edge and label attribute in labels
            if graph.has_edge(u, v) and u != v:  # If exists edge (u, v) in graph and u and v have different values
                if label == 1:  # Equivalence class of 1
                    graph.add_edge(u, v, color='black', style='solid')  # Edge painted black and style is solid
                elif label == 2:  # Equivalence class of 2
                    graph.add_edge(u, v, color='grey', style='solid')  # Edge painted grey and style is solid
                elif label == 3:  # Equivalence class of 4
                    graph.add_edge(u, v, color='green', style='solid')  # Edge painted green and style is solid
                elif label == 4:  # Equivalence class of 4
                    graph.add_edge(u, v, color='magenta', style='solid')  # Edge painted magenta and style is solid
                elif label == 5:  # Equivalence class of 5
                    graph.add_edge(u, v, color='orange', style='solid')  # Edge painted orange and style is solid
                elif label == 6:  # Equivalence class of 6
                    graph.add_edge(u, v, color='blue', style='solid')  # Edge painted blue and style is solid
                elif label == 7:  # Equivalence class of 7
                    graph.add_edge(u, v, color='red', style='solid')  # Edge painted red and style is solid
                elif label == 8:  # Equivalence class of 8
                    graph.add_edge(u, v, color='yellow', style='solid')  # Edge painted yellow and style is solid
                else:  # The others
                    graph.add_edge(u, v, color='brown', style='solid')  # Edge painted brown and style is solid

        return graph

    @staticmethod
    def createLinearGraphWithThreshold(graph, rows, k):
        """
        Create a linear graph with threshold

        :param graph: Networkx's graph
        :param rows: Rows from a SQLite table
        :param k: Threshold
        :type graph: nx.Graph
        :type k: int
        :return: A linear graph with threshold
        :rtype: nx.Graph
        """
        Graph.labeledEdges(graph, rows)  # Labeling edges from graph
        labels = Graph.getLabelAttributesFromGraph(graph)  # Edge labels from graph

        for (u, v), label in labels.items():  # For each edge and label attribute in labels
            if graph.has_edge(u, v) and u != v:  # If exists edge (u, v) in graph and u and v have different values
                if label >= k:  # If label attribute from edge(u, v) is equal or greater than k constant
                    if label == k:  # Equivalence class k
                        graph.add_edge(u, v, color='black', style='solid')  # Edge painted black and style is solid
                    elif label == k + 1:  # Equivalence class k + 1
                        graph.add_edge(u, v, color='grey', style='solid')  # Edge painted grey and style is solid
                    elif label == k + 2:  # Equivalence class k + 2
                        graph.add_edge(u, v, color='green', style='solid')  # Edge painted green and style is solid
                    elif label == k + 3:  # Equivalence class k + 3
                        graph.add_edge(u, v, color='magenta', style='solid')  # Edge painted magenta and style is solid
                    elif label == k + 4:  # Equivalence class k + 4
                        graph.add_edge(u, v, color='orange', style='solid')  # Edge painted orange and style is solid
                    elif label == k + 5:  # Equivalence class k + 5
                        graph.add_edge(u, v, color='blue', style='solid')  # Edge painted blue and style is solid
                    elif label == k + 6:  # Equivalence class k + 6
                        graph.add_edge(u, v, color='red', style='solid')  # Edge painted red and style is solid
                    elif label == k + 7:  # Equivalence class k + 7
                        graph.add_edge(u, v, color='yellow', style='solid')  # Edge painted yellow and style is solid
                    else:  # Equivalence class >= k + 8
                        graph.add_edge(u, v, color='brown', style='solid')  # Edge painted brown and style is solid
                else:
                    graph.remove_edge(u, v)

        return graph

    @staticmethod
    def createExponentialGraph(linearGraph, rows):
        """
        Create a exponential graph

        :param linearGraph: Networkx's graph
        :param rows: Rows from a SQLite table
        :type linearGraph: nx.Graph
        :return: An exponential graph
        :rtype: nx.Graph
        """
        newGraph = Graph.createLinearGraph(linearGraph, rows)  # Create a new graph from linearGraph
        labels = Graph.getLabelAttributesFromGraph(newGraph)  # Edge labels from newGraph

        for (u, v), label in labels.items():  # For each edge and label attribute in labels
            if newGraph.has_edge(u, v) and u != v:  # If exists edge (u, v) in graph and u and v have different values
                if label == 1:  # Equivalence class of 1
                    newGraph.add_edge(u, v, color='black', style='solid')  # Edge painted black and style is solid
                elif 2 <= label < 4:  # Equivalence classes of (2-3)
                    newGraph.add_edge(u, v, color='grey', style='solid')  # Edge painted grey and style is solid
                elif 4 <= label < 8:  # Equivalence classes of (4-7)
                    newGraph.add_edge(u, v, color='green', style='solid')  # Edge painted green and style is solid
                elif 8 <= label < 16:  # Equivalence classes of (8-15)
                    newGraph.add_edge(u, v, color='magenta', style='solid')  # Edge painted magenta and style is solid
                elif 16 <= label < 32:  # Equivalence classes of (16-31)
                    newGraph.add_edge(u, v, color='orange', style='solid')  # Edge painted orange and style is solid
                elif 32 <= label < 64:  # Equivalence classes of (32-63)
                    newGraph.add_edge(u, v, color='blue', style='solid')  # Edge painted blue and style is solid
                elif 64 <= label < 128:  # Equivalence classes of (64-127)
                    newGraph.add_edge(u, v, color='red', style='solid')  # Edge painted red and style is solid
                elif 128 <= label < 256:  # Equivalence classes of (128-255)
                    newGraph.add_edge(u, v, color='yellow', style='solid')  # Edge painted yellow and style is solid
                else:  # The others
                    newGraph.add_edge(u, v, color='brown', style='solid')  # Edge painted brown and style is solid

        return newGraph

    @staticmethod
    def createExponentialGraphWithThreshold(linearGraph, rows, k):
        """
        Create a exponential graph with threshold

        :param linearGraph: Networkx's graph
        :param rows: Rows from a SQLite table
        :param k: Threshold
        :type linearGraph: nx.Graph
        :type k: int
        :return: A exponential graph with threshold
        :rtype: nx.Graph
        """
        newGraph = Graph.createLinearGraphWithThreshold(linearGraph, rows, k)  # Create a new graph from linearGraph
        labels = Graph.getLabelAttributesFromGraph(newGraph)  # Edge labels from graph

        for (u, v), label in labels.items():  # For each edge and label attribute in labels
            if newGraph.has_edge(u, v) and u != v:  # If exists edge (u, v) in graph and u and v have different values
                if label >= k:  # If label attribute from edge(u, v) is equal or greater than k constant
                    if label == k:  # Equivalence class k
                        newGraph.add_edge(u, v, color='black', style='solid')  # Edge painted black and style is solid
                    elif k + 1 <= label < k + 3:  # Equivalence classes (k+1-k+3)
                        newGraph.add_edge(u, v, color='grey', style='solid')  # Edge painted grey and style is solid
                    elif k + 3 <= label < k + 7:  # Equivalence classes (k+3-k+7)
                        newGraph.add_edge(u, v, color='green', style='solid')  # Edge painted green and style is solid
                    elif k + 7 <= label < k + 15:  # Equivalence classes (k+7-k+15)
                        newGraph.add_edge(u, v, color='magenta',
                                          style='solid')  # Edge painted magenta and style is solid
                    elif k + 15 <= label < k + 31:  # Equivalence classes (k+15-k+31)
                        newGraph.add_edge(u, v, color='orange', style='solid')  # Edge painted orange and style is solid
                    elif k + 31 <= label < k + 63:  # Equivalence classes of (k+31-k+63)
                        newGraph.add_edge(u, v, color='blue', style='solid')  # Edge painted blue and style is solid
                    elif k + 63 <= label < k + 127:  # Equivalence classes of (k+63-k+127)
                        newGraph.add_edge(u, v, color='red', style='solid')  # Edge painted red and style is solid
                    elif k + 127 <= label < k + 255:  # Equivalence classes of (k+127-k+255)
                        newGraph.add_edge(u, v, color='yellow', style='solid')  # Edge painted yellow and style is solid
                    else:  # Others
                        newGraph.add_edge(u, v, color='brown', style='solid')  # Edge painted brown and style is solid
                else:
                    graph.remove_edge(u, v)

        return newGraph

    # @staticmethod
    # def getMaxCardinalityFromGraph(graph):
    #     """
    #     Return the max cardinality from graph
    #
    #     :param graph: Networkx's graph
    #     :type graph: nx.Graph
    #     :return: The max cardinality
    #     :rtype: int
    #     """
    #     return nx.graph_clique_number(graph)

    @staticmethod
    def exportGraph(graph, graphName):
        """
        Export a graph to DOT format

        :param graph: Networkx's graph
        :param graphName: Graph name
        :type graph: nx.Graph
        :type graphName: str
        """
        nx.nx_pydot.write_dot(graph, graphName)
