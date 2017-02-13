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

pathBD = str(input("Please enter a path from database file input: "))
conn = sqlite3.connect(pathBD)
# conn = sqlite3.connect('C:/Users/Laura/PycharmProjects/TFG/src/SQL/BD.db')
c = conn.cursor()

pathFile = str(input("Please enter a path from data file input: "))
file = open(pathFile, 'r')
# file = open('C:/Users/Laura/PycharmProjects/TFG/src/SQL/meteo.txt', 'r')
lines = file.readlines()
file.close()

c.execute('CREATE TABLE IF NOT EXISTS test (outlook, temperature, humidity, windy, play)')
for ns in lines:
    d = re.split('\s+', ns, 4)
    c.execute('INSERT OR IGNORE INTO test ( outlook, temperature, humidity, windy, play) VALUES (?, ?, ?, ? , ?)',
              (d[0].split(':')[1], d[1].split(':')[1], d[2].split(':')[1], d[3].split(':')[1], d[4].split(':')[1]))
    conn.commit()
