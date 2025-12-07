import sqlite3

sql_connection = None

try:
    # sql_connection = sqlite3.connect(":memory:")  # baza umieszczona w pamięci
    sql_connection = sqlite3.connect("sqlite_python.db")  # baza w pliku
    cursor = sql_connection.cursor()
    print("Baza zostałą podłączona")

    insert = """
    INSERT INTO software (id,name,price) VALUES (1, 'Python',100);
    """

    insert2 = """
        INSERT INTO software (id,name,price) VALUES (2, 'Java',1000);
        """

    insert3 = """
        INSERT INTO software (id,name,price) VALUES (3, 'C#',10000);
        """

    # cursor.execute(insert)
    # cursor.execute(insert2)
    # cursor.execute(insert3)
    # sql_connection.commit()

    select = """
    SELECT * FROM software;
    """

    # dwa podejscia do select
    # lepsze przy dużej ilości danych
    for row in cursor.execute(select):
        print(row)
        # Baza zostałą podłączona
        # (1, 'Python', 100.0)
        # (2, 'Java', 1000.0)
        # (3, 'C#', 10000.0)
        # Baza zostałą zamknięta

    # przy małeej ilości danych
    cursor.execute(select)
    rows = cursor.fetchall()
    print(rows)
    # [(1, 'Python', 100.0), (2, 'Java', 1000.0), (3, 'C#', 10000.0)]

except sqlite3.Error as e:
    print("Bład bazy danych", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza zostałą zamknięta")

# Baza zostałą podłączona
# Baza zostałą zamknięta
