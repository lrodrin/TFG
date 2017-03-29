from src.final.Data import *
from src.final.Subset import *

if __name__ == '__main__':
    file = Data.openFile('cpu.fq')
    for line in file.readlines():
        print(line[0], line[1])

    Subset.powersetGenerator()