"""
This module implements ...

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'


def makeTree(elements=None):
    if elements is None:
        elements = []
    elementsTree = []
    index = 0

    while index < len(elements):
        # If the next level is greater than current...
        if index + 1 < len(elements) and \
                        elements[index][0] < elements[index + 1][0]:
            # Finds the first and the last index of the direct descendants of
            # the current level.
            level = elements[index][0]
            frm = index + 1

            while index + 1 < len(elements) and \
                            elements[index + 1][0] != level:
                index += 1

            to = index + 1

            # Create a new list with the descendants elements, resolve it, and
            # append as child.
            elementsTree.append(elements[frm - 1][1:] +
                                [makeTree(elements[frm: to])])
        # Just append as is to the list without children elements.
        else:
            # Remove the first item.
            elementsTree.append(elements[index][1:] + [[]])

        index += 1

    return elementsTree


clansList = [{'E'}, {'B'}, {'A'}, {'C'}, {'D'}, {'E', 'D'}, {'E', 'A', 'D'}, {'E', 'B', 'A', 'D'},
             {'E', 'B', 'A', 'C', 'D'}]
print(makeTree(clansList))