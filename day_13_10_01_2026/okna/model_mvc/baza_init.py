import sqlite3


def create_table():
    with sqlite3.connect("app.db") as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT
            );
            """
        )


def insert_init_users():
    with sqlite3.connect("app.db") as conn:
        conn.execute(
            """
            INSERT INTO users (id, name, email) VALUES ('1', 'Radek','radek@wp.pl');
            """
        )
        conn.execute(
            """
            INSERT INTO users (id, name, email) VALUES ('2', 'Tomek','tomek@wp.pl');
            """
        )
        conn.execute(
            """
            INSERT INTO users (id, name, email) VALUES ('3', 'Ania','ania@wp.pl');
            """
        )


if __name__ == '__main__':
    create_table()
    insert_init_users()