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
    def initGraph(tableName, cursor):
        """
        Create and initializes a graph from a table SQLite database source

        :param tableName: Table name
        :param cursor: Cursor object
        :type tableName: str
        :return: A graph
        :rtype: nx.Graph
        """
        graph = nx.Graph()  # Create an empty graph with no nodes and no edges
        columnNames, rows = Data.selectData(tableName, cursor)  # Select data from tableName
        Graph.addNodes(graph, columnNames, rows)  # Adding nodes to graph
        for (u, v) in itertools.combinations(graph.nodes(), 2):  # For the initialization all the edges from graph are
            # painted black and the edge style is dashed
            if u != v:
                graph.add_edge(u, v, color='black', style='dashed')

        return graph, rows

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
    def labeledEdges(graph, rows):
        """
        Count the number of equivalences and label the edges from graph with the total number of equivalences

        :param graph: Networkx's graph
        :param rows: Rows from a SQLite table
        :type graph: nx.Graph
        """
        numberOfEquivalences = dict()
        for row in rows:  # For each row in rows
            for (u, v) in itertools.combinations(row, 2):  # For each pair (u, v) in the row
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

        for (u, v), label in labels.items():  # For each edge and label attribute in labels
            if graph.has_edge(u, v) and u != v:  # If exists edge (u, v) in graph and u and v have different values
                if label > 0:  # If label attribute from edge(u, v) is bigger than 0
                    graph.add_edge(u, v, color='black', style='solid')  # Edge painted black and line style is not
                    # dashed

        return graph

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

        for (u, v), label in labels.items():  # For each edge and label attribute in labels
            if graph.has_edge(u, v) and u != v:  # If exists edge (u, v) in graph and u and v have different values
                if label < k:  # If label attribute from edge(u, v) is smaller than k constant
                    graph.add_edge(u, v, color='black', style='dashed')  # Edge painted black and line style is dashed
                elif label >= k:  # If label attribute from edge(u, v) is equal or greater than k constant
                    graph.add_edge(u, v, color='black',
                                   style='solid')  # Edge painted black and line style is not dashed

        return graph

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
        potentialColors = {1: 'black', 2: 'cyan', 3: 'green', 4: 'magenta', 5: 'orange', 6: 'blue',
                           7: 'red', 8: 'yellow', 9: 'brown', 10: 'grey'}  # Potential colours for equivalence classes

        for label, color in potentialColors.items():  # For each label and color edge attributes in potentialColors
            for (u, v) in graph.edges():  # For each edge from graph
                if graph.has_edge(u, v) and u != v:  # If exists edge (u, v) in graph and u and v have different values
                    if 'label' in graph[u][v] and label == graph[u][v]['label']:  # If edge have the label attribute and
                        # the number of equivalences in potentialColors are the same
                        if graph[u][v]['label'] > 0:  # If the number of equivalences is greater than 0
                            graph.add_edge(u, v, color=color,
                                           style='solid')  # Edge painted with a color from potentialColor and line
                            # style is not dashed

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
                    newGraph.add_edge(u, v, color='black', style='solid')  # Edge painted black and style is dashed
                elif 2 <= label < 4:  # Equivalence classes of (2-3)
                    newGraph.add_edge(u, v, color='cyan', style='solid')  # Edge painted cyan and style is dashed
                elif 4 <= label < 8:  # Equivalence classes of (4-7)
                    newGraph.add_edge(u, v, color='green', style='solid')  # Edge painted green and style is dashed
                elif 8 <= label < 16:  # Equivalence classes of (8-15)
                    newGraph.add_edge(u, v, color='magenta', style='solid')  # Edge painted magenta and style is dashed
                elif 16 <= label < 32:  # Equivalence classes of (16-31)
                    newGraph.add_edge(u, v, color='orange', style='solid')  # Edge painted orange and style is dashed
                elif 32 <= label < 64:  # Equivalence classes of (32-63)
                    newGraph.add_edge(u, v, color='blue', style='solid')  # Edge painted blue and style is dashed
                elif 64 <= label < 128:  # Equivalence classes of (64-127)
                    newGraph.add_edge(u, v, color='red', style='solid')  # Edge painted red and style is dashed
                elif 128 <= label < 256:  # Equivalence classes of (128-255)
                    newGraph.add_edge(u, v, color='yellow', style='solid')  # Edge painted yellow and style is dashed
                elif 256 <= label < 512:  # Equivalence classes of (256-511)
                    newGraph.add_edge(u, v, color='brown', style='solid')  # Edge painted brown and style is dashed
                elif 512 <= label < 1024:  # Equivalence classes of (512-1023)
                    newGraph.add_edge(u, v, color='grey', style='solid')  # Edge painted grey and style is dashed

        return newGraph

    @staticmethod
    def getMaxCardinalityFromGraph(graph):
        """
        Return the max cardinality from graph

        :param graph: Networkx's graph
        :type graph: nx.Graph
        :return: The max cardinality
        :rtype: int
        """
        return nx.graph_clique_number(graph)

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
