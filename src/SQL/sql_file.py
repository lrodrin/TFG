"""
This module implements a table for a database

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
import sqlite3
import re

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

conn = sqlite3.connect('C:/Users/Laura/PycharmProjects/TFG/src/SQL/ex_py_s.db')
c = conn.cursor()

file = open('C:/Users/Laura/PycharmProjects/TFG/src/SQL/dades.txt', 'r')
lines = file.readlines()
file.close()

c.execute('''CREATE TABLE IF NOT EXISTS test (outlook, temperature, humidity, windy, play)''')

for ns in lines:
    d = re.split('\s+', ns, 4)
    c.execute('INSERT INTO test ( outlook, temperature, humidity, windy, play) VALUES (?, ?, ?, ? , ?)',
              (d[0].split(':')[1], d[1].split(':')[1], d[2].split(':')[1], d[3].split(':')[1], d[4].split(':')[1]))
    conn.commit()
