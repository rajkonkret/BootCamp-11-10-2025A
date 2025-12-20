# context manager - narzędzie ułątwiające pracę np.:  z plikami, bazami
# with - context manager w pythonie
# __enter__ - wykonuje się przy uruchomieniu
# __exit__ - wykonuje się przy wyjsciu(niezależnie czy jest bład czy nie)
import sqlite3


class SQLiteDBContextManager:
    def __init__(self, db_name):
        """
        Metoda inicjalizująca, konstruktor
        :param db_name:
        """
        self.db_name = db_name
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):  # wykonuje się zawsze
        if self.conn:
            self.conn.commit()
            self.conn.close()


db_name = "my_data.db"

with SQLiteDBContextManager(db_name) as conn:
    cursor = conn.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT);')
