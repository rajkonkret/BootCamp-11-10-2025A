import sqlite3


class UserModel:
    def add_user(self, name, mail):
        with sqlite3.connect("app.db") as conn:
            conn.execute(
                "INSERT INTO users (name, email) VALUES (?,?)",
                (name, mail)
            )

    def get_users(self):
        with sqlite3.connect('app.db') as conn:
            return conn.execute(
                "SELECT name, email FROM users;"
            ).fetchall()
