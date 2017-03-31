from src.final.Interface import *
from src.final.Clan import *


def convertDataToSet(dataFile):
    """
    Return the more frequent subsets from data file specified by dataFile

    :return: The more frequent subsets
    :rtype: list
    """
    subset = set()
    moreFrequentSubsets = list()
    for line in dataFile.readlines():   # For each line in dataFile
        for word in line.split(" "):    # For each word in line
            if not word.startswith("("):
                subset.add(word)    # Add word as a subset
        moreFrequentSubsets.append(frozenset(subset))
        subset = set()
    return moreFrequentSubsets

def gen(nodes):
    for subset in chain.from_iterable(combinations(nodes, r) for r in range(1, len(nodes) + 1)):
        yield set(subset)

if __name__ == '__main__':
    file = Data.openFile('cpu.fq')  # Open data file parsed with apriori algorithm
    total = convertDataToSet(file) # TODO ha d'anar a la classe Subset

    optionData = int(six.moves.input("Please enter the option for the type of file you provide:\n [1] = ARFF\n [2] = "
                                     "TXT\n [3] = DB\n"))

    columnNames, rows, cursor, tableName = Interface.inputFileOptions(optionData)  # Manages the data entry
    initGraph, rows = Graph.initGraph(tableName, cursor)  # Initialize the g

    optionGraph = int(
        six.moves.input("Please enter the option of g you want to create:\n [1] = plain\n [2] = plain "
                        "with threshold\n [3] = linear\n [4] = exponential\n"))
    g, graphName = Interface.graphOptions(optionGraph, initGraph, rows)  # Create a type of g


    clansList = list()
    for s in total:  # For each s in nodes
        if Clan.isClan(g, s):  # If s is a clan
            clansList.append(s)  # Add s to the clans list

    print(clansList)

