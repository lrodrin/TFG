import itertools

__author__ = "\"Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>"""


def isAClan(Graph, subSet):
    """
    Checks if subset of the graph is a clan

    :param Graph: Networkx's Graph
    :param subSet: Subset from Graph
    :type subSet: set
    :return: b
    :rtype: True if successful, False otherwise
    """
    diff = set(Graph.nodes()).difference(subSet)  # Subset formed by all nodes of graph less subset passed as argument
    b = True
    for external in diff:  # For each subset of diff
        for (x, y) in itertools.combinations(subSet, 2):  # For each pair (x, y) in the subset combinations
            color_x = Graph.edge[external][x]['color']
            color_y = Graph.edge[external][y]['color']
            if color_x != color_y:  # Pair (x, y) not the same colored
                b = False
    return b


def isATrivialClan(subSet):
    """
    Checks if clan is trivial

    :param subSet: It is a subset clan
    :type subSet: set
    :return: b
    :rtype: True if successful, False otherwise
    """
    if len(subSet) == 0 or len(subSet) == 1:  # Empty clan or clan that contains one element
        return True
    else:
        return False
