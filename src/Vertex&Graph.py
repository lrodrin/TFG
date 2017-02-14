#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
This module implements Vertex and Graph class
"""
__all__ = ["add_neighbor", "get_connections", "get_id", "get_weight", "add_vertex", "get_vertex", "add_edge",
           "get_vertices"]
__author__ = "\"Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>"""
#    Copyright (C) 2016 by
#    Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>
#    All rights reserved
#    BSD license


class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        """

        :param neighbor:
        :type weight: int
        """
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    @property
    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]


class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices += 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, color=""):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], color)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], color)

    def get_vertices(self):
        return self.vert_dict.keys()
