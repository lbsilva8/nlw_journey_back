'''Database config'''
import sqlite3
from sqlite3 import Connection


class DbConnectionHandler:
    '''Class designed to handle database connections using SQLite:

    Attributes:
        __connection_string (str): The database file path.
        __conn (sqlite3.Connection): The connection object.
    '''

    def __init__(self) -> None:
        self.__connection_string = "storage.db"
        self.__conn = None

    def connect(self) -> None:
        '''Establishes a connection to the SQLite database.'''
        conn = sqlite3.connect(self.__connection_string,
                               check_same_thread=False)
        self.__conn = conn

    def get_connection(self) -> Connection:
        '''Returns the active database connection.

        Returns:
            sqlite3.Connection: The active database connection.
        '''
        return self.__conn


db_connection_handler = DbConnectionHandler()
