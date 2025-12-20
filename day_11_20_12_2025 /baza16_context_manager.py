# context manager - narzędzie ułątwiające pracę np.:  z plikami, bazami
# with - context manager w pythonie
# __enter__ - wykonuje się przy uruchomieniu
# __exit__ - wykonuje się przy wyjsciu(niezależnie czy jest bład czy nie)
import sqlite3
from pprint import pprint


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
lista = []

with SQLiteDBContextManager(db_name) as conn:
    cursor = conn.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT);')
    cursor.execute("INSERT INTO users (name) VALUES (?);", ("John",))
    cursor.execute("INSERT INTO users (name) VALUES (?);", ("Alice",))
    cursor.execute("INSERT INTO users (name) VALUES (?);", ("Tom",))
    cursor.execute("INSERT INTO users (name) VALUES (?);", ("Radek",))

    # select = cursor.execute("SELECT * FROM  users;")
    select = cursor.execute("SELECT id, name FROM  users;")
    for i in select:
        print(i)
        lista.append(i)

print(lista)
# [(1, 'John'), (2, 'John'), (3, 'Alice'), (4, 'Tom'), (5, 'Radek'), (6, 'John'), (7, 'Alice'), (8, 'Tom'), (9, 'Radek'), (10, 'John'), (11, 'Alice'), (12, 'Tom'), (13, 'Radek')]

pprint(lista)
# [(1, 'John'),
#  (2, 'John'),
#  (3, 'Alice'),
#  (4, 'Tom'),
#  (5, 'Radek'),
#  (6, 'John'),
#  (7, 'Alice'),
#  (8, 'Tom'),
#  (9, 'Radek'),
#  (10, 'John'),
#  (11, 'Alice'),
#  (12, 'Tom'),
#  (13, 'Radek'),
#  (14, 'John'),
#  (15, 'Alice'),
#  (16, 'Tom'),
#  (17, 'Radek')]
