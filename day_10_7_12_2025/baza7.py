import sqlite3

sql_connection = None

try:
    # sql_connection = sqlite3.connect(":memory:")  # baza umieszczona w pamięci
    sql_connection = sqlite3.connect("sqlite_python.db")  # baza w pliku
    cursor = sql_connection.cursor()
    print("Baza zostałą podłączona")

    # update id=7, price 1999
    update = """
    UPDATE software SET price=1999 WHERE id=7;
    """

    # cursor.execute(update)
    # sql_connection.commit()

    delete = """
    DELETE FROM software WHERE id=1;
    """
    cursor.execute(delete)
    sql_connection.commit()

    # price ma być większa niż 2000
    select = """
    SELECT * FROM software WHERE price > 2000;
    """

    cursor.execute(select)
    rows = cursor.fetchall()
    for r in rows:
        print(r)
    # Baza zostałą podłączona
    # (3, 'C#', 10000.0)
    # (4, 'Scala', 5600.0)
    # Baza zostałą zamknięta

except sqlite3.Error as e:
    print("Bład bazy danych", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza zostałą zamknięta")

# Baza zostałą podłączona
# Baza zostałą zamknięta
