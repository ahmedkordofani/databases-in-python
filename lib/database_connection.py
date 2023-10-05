import psycopg
from psycopg.rows import dict_row
import os

class DatabaseConnection:
    DATABASE_NAME = "music_library"

    def __init__(self):
        self.connection_string = f"postgresql://localhost/{self.DATABASE_NAME}"

    def connect(self):
        try:
            self.connection = psycopg.connect(
                self.connection_string,
                row_factory=dict_row
            )
        except psycopg.OperationalError:
            raise Exception(f"Couldn't connect to the database {self.DATABASE_NAME}! "
                            f"Did you create it using `createdb {self.DATABASE_NAME}`?")

    def seed(self, sql_filename):
        self._check_connection()
        if not os.path.exists(sql_filename):
            raise Exception(f"File {sql_filename} does not exist")
        with self.connection.cursor() as cursor:
            cursor.execute(open(sql_filename, "r").read())
            self.connection.commit()

    def execute(self, query, params=None):
        self._check_connection()
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            if cursor.description is not None:
                result = cursor.fetchall()
            else:
                result = None
            self.connection.commit()
            return result

    def _check_connection(self):
        if self.connection is None:
            raise Exception("DatabaseConnection.exec_params: Cannot run a SQL query as "
                            "the connection to the database was never opened. Did you "
                            "make sure to call the method DatabaseConnection.connect in your app.py file (or in your tests)?")
