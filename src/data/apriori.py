from src.final.Interface import *


def convertToSet():
    global s
    result = list()
    for line in file.readlines():
        for word in line.split(" "):
            if not word.startswith("("):
                s.add(word)
        result.append(frozenset(s))
        print(s)
        s = set()
    return result


if __name__ == '__main__':
    s = set()
    file = Data.openFile('test.txt')
    total = convertToSet()

    optionData = int(six.moves.input("Please enter the option for the type of file you provide:\n [1] = ARFF\n [2] = "
                                     "TXT\n [3] = DB\n"))

    columnNames, rows, cursor, tableName = Interface.inputFileOptions(optionData)  # Manages the data entry
    initGraph, rows = Graph.initGraph(tableName, cursor)  # Initialize the graph

    optionGraph = int(
        six.moves.input("Please enter the option of graph you want to create:\n [1] = plain\n [2] = plain "
                        "with threshold\n [3] = linear\n [4] = exponential\n"))
    graph = Interface.graphOptions(optionGraph, initGraph, rows)  # Create a type of graph

    clansList = Clan.clans(graph, total)  # Create clans list
    print(clansList)
