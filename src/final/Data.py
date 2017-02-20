"""
This module implements the Data class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
import sqlite3

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'


class Data:
    @staticmethod
    def connection(db_file):
        """
            Create a database connection to the SQLite database specified by db_file

        :param db_file: Database file
        :return: Connection object or None
        """
        try:
            connection = sqlite3.connect(db_file)
            print("Connection performed to", db_file)
            return connection
        except sqlite3.Error as e:
            print("Error:", e)

        return None

    @staticmethod
    def open_file(path):
        """
            Open a file from path specified by path

        :param path: Path to file
        :return: File object or None
        """
        try:
            file = open(path, 'r')
            print("File opened from", path)
            return file
        except IOError as e:
            print("Error:", e)

        return None

    @staticmethod
    def get_data_from_file(file):
        """
            Get column names and all lines from file

        :param file: File
        :return: Column names and lines
        """
        colNames = ""
        lines = file.readlines()  # Keep all lines from data file into lines
        header = lines[0]  # Extract the header from lines
        for word in header.split(" "):  # For each word from header
            colNames += word + ", "  # Adding a column into colNames
        return colNames, lines

    @staticmethod
    def create_table(cursor, tableName, colNames):
        """
            Create a table for SQLite database

        :param cursor: Connection cursor to database
        :param tableName: Table name
        :param colNames: Column names
        """
        try:
            query = "CREATE TABLE %s (%s);" % (str(tableName), str(colNames[0:-2]))  # SQL query
            cursor.execute(query)
            print("Table %s created" % tableName)
        except sqlite3.Error as e:
            print("Error:", e)

    @staticmethod
    def insert(tableName, colNames, lines, cursor, connection):
        """
            Insert values to table tableName for SQLite database

        :param tableName: Table name
        :param colNames: Column names
        :param lines: Lines from data file
        :param cursor: Connection cursor
        :param connection: Connection object
        """
        values = ""
        for i in range(1, len(lines)):  # For each row from data file
            for col in lines[i].split(" "):  # For each column in lines[i]
                values += "'%s'," % col.split(":")[1]  # Extract and save the values
            try:
                query = 'INSERT INTO {0} ({1}) VALUES ({2});'.format(str(tableName), str(colNames[0:-2]),
                                                                     str(values[0:-1]).replace('\n', ''))
                # SQL query
                cursor.execute(query)
                print("Row[%d] inserted" % i)
                connection.commit()
            except sqlite3.Error as e:
                print("Error:", e)
            values = ""

    @staticmethod
    def close(file, cursor, connection):
        """
            Close the open file, cursor and connection database
        :param file: File
        :param cursor: Connection cursor
        :param connection: Connection object
        """
        try:
            file.close()
            print("File closed")
        except IOError as e:
            print("Error:", e)
        try:
            cursor.close()
        except IOError as e:
            print("Error:", e)
        try:
            connection.close()
            print("Connection closed")
        except IOError as e:
            print("Error:", e)
