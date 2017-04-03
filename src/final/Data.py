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
    # TODO tractar diferents taules

    @staticmethod
    def connectionDB(fileDB):
        """
        Create a database connection to the SQLite database specified by fileDB

        :param fileDB: Database SQLite file
        :type fileDB: str
        :return: Connection object and cursor object or None
        """
        try:
            dbName = fileDB + ".db"
            connection = sqlite3.connect(dbName)
            cursor = connection.cursor()
            print("Connection successful to", dbName)

            return connection, cursor

        except sqlite3.Error as e:
            print("Error to connection:", e)

        return None

    @staticmethod
    def openFile(dataFile):
        """
        Open data file specified by dataFile

        :param dataFile: Data file
        :type dataFile: str
        :return: File object or None
        :rtype: file
        """
        try:
            file = open(dataFile, 'r')
            print("File %s opened" % dataFile)

            return file

        except IOError as e:
            print("Error to open file:", e)

        return None

    @staticmethod
    def getDataFile(dataFile, fileType):
        """
        Get data from data file specified by dataFile

        :param dataFile: Data file
        :param fileType: File type
        :type dataFile: file
        :type fileType: str
        :return: Column names and lines from dataFile
        """
        columnNames = str()
        lines = dataFile.readlines()  # Extract all the lines from dataFile
        if fileType == "TXT":
            header = lines[0].replace("\n", "")  # Extract the header line from dataFile
            for word in header.split(" "):  # For each word in header
                columnNames += word + ", "  # Adding column name into columnNames
        elif fileType == "ARFF":
            for line in lines:  # For each line in lines
                if line.startswith("@attribute"):  # If is an attribute
                    columnNames += line.split(" ")[1] + ", "  # Adding column name into columnNames

        return columnNames, lines

    @staticmethod
    def createTable(cursor, tableName, columnNames):
        """
        Create a table specified by tableName in a SQLite database

        :param cursor: Connection cursor
        :param tableName: Table name
        :param columnNames: Column names
        :type tableName: str
        :type columnNames: str
        """
        try:
            query = 'CREATE TABLE {0} ({1});'.format(str(tableName), str(columnNames[0:-2]))
            cursor.execute(query)
            # print(query)
        except sqlite3.Error as e:
            print("Error to create table:", e)

    @staticmethod
    def insertDataTXT(tableName, columnNames, lines, cursor, connection):
        """
        Insert values to a table specified by tableName in a SQLite database from a TXT file

        :param tableName: Table name
        :param columnNames: Column names
        :param lines: Lines from a data file
        :param cursor: Cursor object
        :param connection: Connection object
        :type tableName: str
        :type columnNames: str
        """
        values = str()
        for line in range(1, len(lines)):  # For each line in lines
            for column in lines[line].split(" "):  # For each column in lines[line]
                if ":" in column:
                    values += "'%s'," % column.split(":")[1]  # Extract values, separator values is :
                elif "=" in column:
                    values += "'%s'," % column.split("=")[1]  # Extract values, separator values is =
            try:
                query = 'INSERT INTO {0} ({1}) VALUES ({2});'.format(str(tableName), str(columnNames[0:-2]),
                                                                     str(values[0:-1]).replace('\n', ''))
                cursor.execute(query)
                connection.commit()
                # print(query)
                values = str()

            except sqlite3.Error as e:
                print("Error to insert in txt file:", e)

    @staticmethod
    def insertDataARFF(tableName, columnNames, lines, cursor, connection):
        """
        Insert values to a table specified by tableName in SQLite database from an ARFF file

        :param tableName: Table name
        :param columnNames: Column names
        :param lines: Lines from a data file
        :param cursor: Cursor object
        :param connection: Connection object
        :type tableName: str
        :type columnNames: str
        """
        values = str()
        for line in lines:  # For each line in lines
            if len(line) != 0:  # If line is not empty
                if not line.startswith("@") and not line.startswith("\n") and not line.startswith("%"):  # Parse init
                    #  line
                    for word in line.split(","):  # For each word in line parsed
                        word = "'{0}'".format(word.replace('\n', ''))  # Quit end of line from word
                        values += word + ','  # Add word to values
                    try:
                        query = 'INSERT INTO {0} ({1}) VALUES ({2})'.format(str(tableName), str(columnNames[0:-2]),
                                                                            str(values[0:-1]).replace('\n', ''))
                        cursor.execute(query)
                        connection.commit()
                        # print(query, line)
                        values = str()

                    except sqlite3.Error as e:
                        print("Error to insert in arff file:", e)

    @staticmethod
    def selectData(tableName, cursor):
        """
        Select all the rows from a table specified by tableName

        :param tableName: Table name
        :param cursor: Cursor object
        :type tableName: str
        :return: Column names and all rows from tableName or None
        """
        try:
            query = 'SELECT * FROM {0};'.format(str(tableName))
            cursor.execute(query)
            columnNames = [description[0] for description in cursor.description]  # Extract column names
            rows = cursor.fetchall()  # All the rows

            return columnNames, rows

        except sqlite3.Error as e:
            print("Error to select in table name %s: %s" % (tableName, e))

        return None

    @staticmethod
    def getTableNameARFF(lines):
        """
        Return the table name from an arff data file

        :param lines: Lines from a data file
        :return: A Table name
        """
        for line in lines:  # For each line in lines
            if line.startswith("@relation"):  # If line starts with @relation
                if "'" in line:  # If table name contains the char '
                    line = line.split(" ")[1]  # Quit the char '
                    return line[1:-2]

                else:  # If table name not contains the char '
                    return line.split(" ")[1]

    @staticmethod
    def getTableNamesDB(cursor):
        """
        Return a list of all the table names from a SQLite database
        
        :param cursor: Cursor object
        :return: List of table names
        :rtype: list
        """
        tablesNameList = list()
        query = "SELECT name FROM sqlite_master WHERE type='table' ORDER BY Name"
        cursor.execute(query)
        tables = map(lambda t: t[0], cursor.fetchall())
        for table in tables:
            tablesNameList.append(table)  # Add table name to the list tablesNameList

        return tablesNameList

    @staticmethod
    def convertDataToSet(dataFile):
        """
        Convert lines from data file specified by dataFile to sets

        :param dataFile: Data file
        :type dataFile: file
        :return: List of all the lines converted to sets
        :rtype: list
        """
        subset = set()
        moreFrequentSubsets = list()
        for line in dataFile.readlines():  # For each line in dataFile
            for word in line.split(" "):  # For each word in line
                if not word.startswith("("):  # If word not contains the char (
                    subset.add(word)  # Add word as a subset
            moreFrequentSubsets.append(frozenset(subset))  # Add subset in list moreFrequentSubsets
            subset = set()

        return moreFrequentSubsets
