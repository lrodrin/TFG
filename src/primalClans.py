from collections import defaultdict

__author__ = "\"Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>"""


def primalClans(listClans):
    """
        Returns a list with the primal clans

        :param listClans: List of clans
        :type listClans: list of sets
        :return: primals
        :rtype: list
    """
    potential_primals = defaultdict(bool)  # Creates and initializes a dictionary from a list of clans
    primals = []  # Empty list
    for i, key in enumerate(listClans):  # For each elem in listClans
        for j in range(i + 1, len(listClans)):  # For each elem+1 in listClans
            intersection = listClans[i] & listClans[j]
            if len(intersection) == 0 or intersection == listClans[i] or intersection == listClans[j]:
                # If not exist overlapping mark the value of potential_primals True
                potential_primals[frozenset(listClans[i])] = True
                potential_primals[frozenset(listClans[j])] = True

    for key, value in potential_primals.items():  # Creates a list with a primal clans of potential_primals
        if potential_primals[key]:  # If is a primal clan
            primals.append(key)  # Add clan to primals list
    return primals
