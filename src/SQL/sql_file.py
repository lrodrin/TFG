"""
This module implements ...

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
import sqlite3

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

conn = sqlite3.connect('C:/Users/Laura/PycharmProjects/TFG/src/SQL/ex_py_s.db')
c = conn.cursor()

for row in c.execute('SELECT * FROM names'):
    print(row)
