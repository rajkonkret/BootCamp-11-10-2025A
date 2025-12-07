import sqlite3

sql_connection = None
lista = []
try:
    # sql_connection = sqlite3.connect(":memory:")  # baza umieszczona w pamięci
    sql_connection = sqlite3.connect("sqlite_python.db")  # baza w pliku

    sql_connection.row_factory = sqlite3.Row  # baza zwróci dane jako słownik

    cursor = sql_connection.cursor()
    print("Baza zostałą podłączona")

    select = """
    SELECT * FROM software;
    """

    for row in cursor.execute(select):
        print(row)  # <sqlite3.Row object at 0x109c671f0>
        lista.append(dict(row))

    print(lista)
    # [{'id': 1, 'name': 'Python', 'price': 100.0},
    # {'id': 2, 'name': 'Java', 'price': 1000.0},
    # {'id': 3, 'name': 'C#', 'price': 10000.0}]

    cursor.execute(select)
    rows = cursor.fetchall()
    for row in rows:
        print(dict(row))
    # {'id': 1, 'name': 'Python', 'price': 100.0}
    # {'id': 2, 'name': 'Java', 'price': 1000.0}
    # {'id': 3, 'name': 'C#', 'price': 10000.0}
except sqlite3.Error as e:
    print("Bład bazy danych", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza zostałą zamknięta")

# Baza zostałą podłączona
# Baza zostałą zamknięta
