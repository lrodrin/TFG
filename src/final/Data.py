"""
This module implements the Data class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
import sqlite3

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'


# TODO el nom de la taula es podria treure amb el @relation

class Data:
    @staticmethod
    def connection(fileDB):
        """
        Create a database connection to the SQLite database specified by fileDB

        :param fileDB: Database SQLite file
        :return: Connection object or None
        """
        try:
            connection = sqlite3.connect(fileDB)
            cursor = connection.cursor()
            print("Connection successful to", fileDB)
            return connection, cursor
        except sqlite3.Error as e:
            print("Error connection:", e)

        return None

    @staticmethod
    def openFile(dataFile):
        """
        Open data file specified by dataFile

        :param dataFile: Data file
        :return: File object or None
        """
        try:
            file = open(dataFile, 'r')
            print("File opened from", dataFile)
            return file
        except IOError as e:
            print("Error open:", e)

        return None

    @staticmethod
    def getDataFile(dataFile):
        """
        Get column names and all lines from file specified by dataFile

        :param dataFile: Data file
        :return: Column names and lines from dataFile
        """
        columnNames = ""
        lines = dataFile.readlines()  # Keep all lines from dataFile into lines
        header = lines[0]  # Extract the header line from dataFile
        for word in header.split(" "):  # For each word in header
            columnNames += word + ", "  # Adding column name into columnNames
        return columnNames, lines

    @staticmethod
    def getDataARFFile(dataFile):
        """
        Get column names and all lines from file specified by dataFile

        :param dataFile: Data file
        :return: Column names and lines from dataFile
        """
        lines = dataFile.readlines()
        columnNames = str()
        for line in lines:
            if line.startswith("@attribute"):
                columnNames += line.split(" ")[1] + ", "
        return columnNames, lines

    @staticmethod
    def createTable(cursor, tableName, columnNames):
        """
        Create a table specified by tableName in SQLite database

        :param cursor: Connection cursor
        :param tableName: Table name
        :param columnNames: Column names
        """
        try:
            query = "CREATE TABLE %s (%s);" % (str(tableName), str(columnNames[0:-2]))  # SQLite query
            cursor.execute(query)
            print("Table %s was created" % tableName)
        except sqlite3.Error as e:
            print("Error create:", e)

    @staticmethod
    def createTableARFF(cursor, tableName, columnNames):
        """
        Create a table specified by tableName in SQLite database

        :param cursor: Connection cursor
        :param tableName: Table name
        :param columnNames: Column names
        """
        try:
            query = "CREATE TABLE %s (%s);" % (str(tableName), str(columnNames[0:-2]))
            cursor.execute(query)
            print("Table %s was created" % tableName)
        except sqlite3.Error as e:
            print("Error create:", e)

    @staticmethod
    def insert(tableName, columnNames, lines, cursor, connection):
        """
        Insert values to table specified by tableName in SQLite database

        :param tableName: Table name
        :param columnNames: Column names
        :param lines: Lines from a data file
        :param cursor: Connection cursor
        :param connection: Connection object
        """
        values = ""
        for line in range(1, len(lines)):  # For each line from data file
            for column in lines[line].split(" "):  # For each column in lines[line]
                values += "'%s'," % column.split(":")[1]  # Extract and keep values in values
            try:
                query = 'INSERT INTO {0} ({1}) VALUES ({2});'.format(str(tableName), str(columnNames[0:-2]),
                                                                     str(values[0:-1]).replace('\n', ''))
                # SQLite query
                cursor.execute(query)
                connection.commit()
                print("Row[%d] %s inserted" % (line, query))
            except sqlite3.Error as e:
                print("Error insert:", e)
            values = ""

    @staticmethod
    def insertARFF(tableName, columnNames, lines, cursor, connection):
        """
        Insert values to table specified by tableName in SQLite database

        :param tableName: Table name
        :param columnNames: Column names
        :param lines: Lines from a data file
        :param cursor: Connection cursor
        :param connection: Connection object
        """
        values = str()
        for line in lines:
            if not line.startswith("@") and not line.startswith("\n") and not line.startswith("%"):
                for word in line.split(","):
                    word = "'{0}'".format(word.replace('\n', ''))
                    values += word + ','
                try:
                    query = 'INSERT INTO {0} ({1}) VALUES ({2})'.format(str(tableName), str(columnNames[0:-2]),
                                                                        str(values[0:-1]).replace('\n', ''))
                    cursor.execute(query)
                    connection.commit()
                    print("Row %s inserted" % query)
                    values = str()
                except sqlite3.Error as e:
                    print("Error insert:", e)

    @staticmethod
    def select(tableName, cursor):
        """
        Select rows from a table specified by tableName in SQLite database

        :param tableName: Table name
        :param cursor: Connection cursor
        :return: Column names and all rows from tableName
        """
        try:
            cursor.execute("SELECT * FROM %s" % tableName)
            columnNames = [description[0] for description in cursor.description]
            rows = cursor.fetchall()
            return columnNames, rows
        except sqlite3.Error as e:
            print("Error select:", e)

        return None

    @staticmethod
    def close(dataFile, cursor, connection):
        """
        Close opened data file, cursor connection and connection to SQLite database

        :param dataFile: Data file
        :param cursor: Connection cursor
        :param connection: Connection object
        """
        error = "Error close:"
        try:
            dataFile.close()
        except IOError as e:
            print(error, e)
        try:
            cursor.close()
        except sqlite3.Error as e:
            print(error, e)
        try:
            connection.close()
        except sqlite3.Error as e:
            print(error, e)

    @staticmethod
    def getTableNameARFF(lines):
        for line in lines:
            if line.startswith("@relation"):
                if "'" in line:
                    line = line.split(" ")[1]
                    return line[1:-2]
                else:
                    return line.split(" ")[1]

    @staticmethod
    def geTablesNames(cursor):
        tablesNameList = list()
        query = "SELECT name FROM sqlite_master WHERE type='table' ORDER BY Name"
        cursor.execute(query)
        tables = map(lambda t: t[0], cursor.fetchall())
        for table in tables:
            tablesNameList.append(table)
        return tablesNameList