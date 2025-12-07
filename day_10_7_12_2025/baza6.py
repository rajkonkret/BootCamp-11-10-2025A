import sqlite3

data = [
    (5, "Rust", 899),
    (6, 'Angular', 1899),
    (7, "JS", 99),
    (8, "Pandas", 199)
]

sql_connection = None

try:
    # sql_connection = sqlite3.connect(":memory:")  # baza umieszczona w pamięci
    sql_connection = sqlite3.connect("sqlite_python.db")  # baza w pliku
    cursor = sql_connection.cursor()
    print("Baza zostałą podłączona")

    insert = """
    INSERT INTO software (id, name, price) VALUES (?,?,?);
    """

    # wpisywanie danych do bazy danych ze zmiennych
    # cursor.execute(insert, (4, "Scala", 5600))
    # sql_connection.commit()

    # wrzucenie danych do bazy danych z listy
    cursor.executemany(insert, data)
    sql_connection.commit()

except sqlite3.Error as e:
    print("Bład bazy danych", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza zostałą zamknięta")

# Baza zostałą podłączona
# Baza zostałą zamknięta
# (.venv) radoslawjaniak@mac day_10_7_12_2025 % sqlite3 sqlite_python.db
# SQLite version 3.51.0 2025-06-12 13:14:41
# Enter ".help" for usage hints.
# sqlite> .tables
# developers  hardware    software
# sqlite> select * from software;
# 1|Python|100.0
# 2|Java|1000.0
# 3|C#|10000.0
# 4|Scala|5600.0
# 5|Rust|899.0
# 6|Angular|1899.0
# 7|JS|99.0
# 8|Pandas|199.0
# sqlite>