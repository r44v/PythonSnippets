# System imports
import sqlite3
import os
from time import time


# Program
class DbHandler:
    __TABLE = 'urls'
    __FIELDS = ["url"]

    # Declare filename
    __dbFileName = "database.db"
    __dbConnection = False

    def __init__(self, db_name=None, read_only=True):
        self.__read_only = read_only
        # Set alternative db file
        if db_name is not None:
            self.__dbFileName = db_name

        # Create db if absent and connect
        if not self.__db_exists():
            self.__connect_to_db(read_only=False)
            self.__create_schema()
            self.close_connection()

        self.__connect_to_db(read_only)

    def __db_exists(self):
        exists = os.path.isfile(self.__dbFileName)
        return exists

    # connect to db (possibly creates file now)
    def __connect_to_db(self, read_only):
        if read_only:
            self.__dbConnection = sqlite3.connect('file:' + self.__dbFileName + '?mode=ro', uri=True)
        else:
            self.__dbConnection = sqlite3.connect(self.__dbFileName)

    def close_connection(self):
        self.__dbConnection.close()

    def __create_schema(self):
        fields = ""
        for field in self.__FIELDS:
            fields += "`"+field+"` TEXT NOT NULL, "

        self.__dbConnection.execute(
            '''CREATE TABLE `'''
            + self.__TABLE+'''` (`id` INTEGER, '''
            + fields
            + '''`created_at` timestamp default CURRENT_TIMESTAMP, '''
            + '''`updated_at` timestamp default CURRENT_TIMESTAMP, '''
            + '''PRIMARY KEY(`id`) );''')

        self.__dbConnection.commit()

    @staticmethod
    def get_timestamp():
        return str(int(time()))

    @staticmethod
    def update_timestamp():
        return ''', `updated_at` = CURRENT_TIMESTAMP'''

    def get(self, row_id):
        res = self.__dbConnection.execute('SELECT * FROM `'+self.__TABLE+'` WHERE `id`=?', [row_id])
        res = res.fetchone()

        return res

    # prepare values
    # values_to_insert = ["", ""]
    def add(self, url):
        self.__dbConnection.execute(
            """
INSERT INTO `"""+self.__TABLE+"""` (`url`)
VALUES ( ? );
        """, [url])

        # save insert
        self.__dbConnection.commit()

    def change_url(self, row_id, url):
        self.__dbConnection.execute('UPDATE `'
                                          + self.__TABLE
                                          + '` SET `url`=?'
                                          + self.update_timestamp()
                                          + ' WHERE `id`=?', [url, row_id])
        self.__dbConnection.commit()

    def get_all(self):
        res = self.__dbConnection.execute('SELECT * FROM `' + self.__TABLE + '`;')
        res = res.fetchall()

        if res is None:
            return []
        else:
            return res