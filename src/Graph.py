#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
This module implements Graph class
"""
__all__ = ["vertices", "edges", "add_vertex", "add_edge"]
__author__ = "\"Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>"""


#    Copyright (C) 2016 by
#    Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>
#    All rights reserved
#    BSD license


class Graph(object):
    def __init__(self, graph_dict=None):
        """ initializes a initGraph object
            If no dictionary or None is given, an empty dictionary will be used """
        if graph_dict is None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        """ returns the vertices of a initGraph """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ returns the edges of a initGraph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in self.__graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary. Otherwise nothing has to be done. """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list between two vertices can be multiple edges """
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        """ A static method generating the edges of the initGraph "initGraph". Edges are represented as sets
            with one (a loop back to the vertex) or two vertices """
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res
