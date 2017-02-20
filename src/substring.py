"""
This module implements ...

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

file = open('C:/Users/Laura/PycharmProjects/TFG/src/SQL/meteo.txt', 'r')  # Open data file
lines = file.readlines()  # Keep all lines from data file into lines

l = ""
for i in range(1, len(lines)):
    for j in lines[i].split(" "):
        l += "'%s'," % j.split(":")[1]
    print(l[0:-1])
    l = ""
file.close()