import psycopg2
from psycopg2.extras import RealDictCursor
from typing import Callable
from psycopg2 import DatabaseError

# Cursor = Callable[...,psycopg2.connect().cursor]


class Connection:

    def __init__(self, database_connection, cursor) -> None:
        self.database = database_connection
        self.cursor = cursor


class DBManager:

    def __init__(self, dbname: str, user: str, password: str) -> None:
        self.dbname = dbname
        self.user = user
        self.password = password

    def connect(self):
        """Create Connection to the Postgre database using Json File have the required data in it 
        - dbname
        - user
        - password (if there was)
        return Curser Object or 0 if Can't """
        try:
            conn = psycopg2.connect(dbname=self.dbname, user=self.user,
                                    password=self.password, cursor_factory=RealDictCursor)
            return Connection(conn, conn.cursor())
        except DatabaseError as e:
            print(f"database cann't connect {e}")


class Controller:
    """inject-> DBManager"""

    def __init__(self) -> None:
        ...
