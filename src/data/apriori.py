from src.final.Interface import *

if __name__ == '__main__':
    optionData = int(six.moves.input("Please enter the option for the type of file you provide:\n [1] = ARFF\n [2] = "
                                     "TXT\n [3] = DB\n"))
    columnNames, rows, cursor, tableName = Interface.inputFileOptions(optionData)  # Manages the data entry
    initGraph, rows = Graph.initGraph(tableName, cursor)  # Initialize a graph

    optionGraph = int(
        six.moves.input("Please enter the option of g you want to create:\n [1] = plain\n [2] = plain "
                        "with threshold\n [3] = linear\n [4] = exponential\n"))
    graph, graphName = Interface.graphOptions(optionGraph, initGraph, rows)  # Create a type of graph

    moreFrequentSubsets = Subset.moreFrequentSubsets(tableName)  # Return the more frequents subsets from file
    clansList = Clan.frequentClans(graph, moreFrequentSubsets)
    print(clansList)
    trivialClansList = Clan.trivialClans(clansList, Graph.getMaxCardinalityFromGraph(graph))
    print(clansList)
    primalClansList = Clan.primalClans(clansList)
    print(primalClansList)
    # Clan.printFrequentResults(graph, moreFrequentSubsets)
