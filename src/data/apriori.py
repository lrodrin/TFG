from src.final.Data import *


def convertToSet():
    global s
    total = list()
    for line in file.readlines():
        for word in line.split(" "):
            if not word.startswith("("):
                s.add(word)
        total.append(s)
        print(s)
        s = set()
    return total


if __name__ == '__main__':
    s = set()
    file = Data.openFile('test.txt')
    print(convertToSet())

    # for subset in Subset.powersetGenerator(set(total)):
    #     print(subset)
