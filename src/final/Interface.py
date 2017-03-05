"""
This module implements the Interface class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'


@staticmethod
def graphOptions(option, graph, rows):
    if option == 1:
        g.Graph.createPlanarGraph(graph, rows)
    elif option == 2:
        g.Graph.linearGraph(graph, rows)
    elif option == 3:
        g.Graph.exponentialGraph(graph, rows)


@staticmethod
    def openGraphviz(program, filename):
        """
            Call the Graphviz program that is associated with a 2-structure file

        :param program: Path to Graphviz program
        :param filename: Path to 2-structure file
        """
        if sys.platform == 'win32':  # Windows platform
            os.startfile(filename)
        else:  # Linux platform
            subprocess.run(['open', '-a', program, filename])