"""
This module implements a Erdös-Rényi Graph with color sequence and labels

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
import random
import networkx as nx
from matplotlib import pyplot as plt

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

# Data input
n = int(input("Please enter a number of nodes: "))
p = float(input("Please enter a probability for the creation of edges: "))
c = int(input("Please enter a number of colors: "))

# Verifying data input
colors_list = ['mediumpurple', 'indianred', 'lightcyan', 'sandybrown', 'linen',
               'palevioletred', 'lavenderblush', 'darkslategrey', 'darkturquoise', 'mistyrose',
               'forestgreen', 'brown', 'salmon', 'blanchedalmond', 'lavender', 'khaki', 'paleturquoise',
               'aquamarine', 'dimgray', 'lime', 'crimson', 'limegreen', 'blue',
               'darkblue', 'aqua', 'yellowgreen', 'mediumturquoise', 'papayawhip', 'peru', 'lightseagreen',
               'sage', 'lightpink', 'darksalmon', 'indigo', 'darksage', 'magenta',
               'maroon', 'gray', 'midnightblue', 'powderblue', 'darkseagreen', 'navy', 'darkorchid', 'red', 'oldlace',
               'darkslateblue', 'skyblue', 'plum', 'burlywood', 'moccasin', 'saddlebrown', 'gold', 'turquoise',
               'darkgreen', 'lightcoral', 'chartreuse', 'lightgray', 'palegreen', 'palegoldenrod', 'dodgerblue',
               'lightsteelblue', 'deepskyblue', 'purple', 'darkkhaki', 'hotpink', 'darkslategray', 'steelblue',
               'lightsage', 'cornsilk', 'lightslategray', 'mediumorchid', 'olive', 'deeppink', 'orchid',
               'pink', 'rosybrown', 'mediumslateblue', 'mediumaquamarine', 'tomato', 'yellow',
               'lightslategrey', 'gainsboro', 'darkgrey', 'slateblue', 'darkviolet', 'mediumvioletred', 'coral',
               'lightgoldenrodyellow', 'mediumseagreen', 'mediumspringgreen', 'peachpuff', 'chocolate', 'slategrey',
               'mediumblue', 'lightgreen', 'orange', 'tan', 'greenyellow', 'darkorange', 'blueviolet',
               'lightskyblue', 'darkolivegreen', 'darkgoldenrod', 'green', 'black', 'seagreen', 'darkmagenta',
               'darkred', 'thistle', 'grey', 'cyan', 'firebrick', 'fuchsia', 'orangered', 'bisque',
               'beige', 'goldenrod', 'cadetblue', 'wheat', 'darkcyan', 'olivedrab', 'darkgray', 'cornflowerblue',
               'lightsalmon', 'sienna', 'slategray', 'royalblue', 'lightblue', 'lemonchiffon', 'violet',
               'dimgrey', 'lawngreen', 'lightgrey', 'springgreen']

if c > len(colors_list):
    print("Ups! It is not a valid number. The number of colors may not be greater than %d! Try it again ..." % len(
        colors_list))
    c = int(input("Please enter a number of colors: "))

# Graph generator
G = nx.erdos_renyi_graph(n, p)

# For each edge of G the color attribute is assigned randomly
for (u, v) in G.edges():
    G.edge[u][v]['color'] = random.choice(colors_list[0:c])

# Color sequence with the same length as G.edges()
edge_color_list = [G[u][v]['color'] for (u, v) in G.edges()]

# Drawing with the color sequence
# nx.draw(G, edge_color=edge_color_list)
# plt.suptitle("Erdös-Rényi Graph with color sequence", fontsize=11)
nx.draw(G, edge_color=edge_color_list, with_labels=nx.spring_layout(G))
plt.suptitle("Erdös-Rényi Graph with color sequence and labels", fontsize=11)
plt.show()

nx.nx_pydot.write_dot(G, 'erdos_renyi_Graphviz_colors.dot')
