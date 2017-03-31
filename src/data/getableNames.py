"""
This module obtain the names from SQLite database tables

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
from src.final.Data import *

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

connection, cursor = Data.connectionDB('C:/Users/Laura/PycharmProjects/TFG/src/final/DB.db')


def geTablesNames():
    query = "SELECT name FROM sqlite_master WHERE type='table' ORDER BY Name"
    cursor.execute(query)
    tables = map(lambda t: t[0], cursor.fetchall())
    for table in tables:
        print(table)


geTablesNames()
