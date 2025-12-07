import sqlite3
from string import Template

sql_connection = None

try:
    # sql_connection = sqlite3.connect(":memory:")  # baza umieszczona w pamięci
    sql_connection = sqlite3.connect("sqlite_python.db")  # baza w pliku
    cursor = sql_connection.cursor()
    print("Baza zostałą podłączona")

    table_name = "software"
    # table_name = "hardware"

    select = f"SELECT * from {table_name}"

    # rozwiązanie z pythona 3.14
    # tmpl = t"SELECT * FROM $table_name;"
    # query = tmpl.substitute(table=table_name)
    # print(query)
    # bezpieczniejsze niz f-string
    tmpl = Template("SELECT * from $table_name;").substitute(table_name=table_name)
    print(tmpl)  # SELECT * from hardware;

    # cursor.execute(select)
    cursor.execute(tmpl)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

except sqlite3.Error as e:
    print("Bład bazy danych", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza zostałą zamknięta")

# Baza zostałą podłączona
# Baza zostałą zamknięta
# Baza zostałą podłączona
# (2, 'Java', 1000.0)
# (3, 'C#', 10000.0)
# (4, 'Scala', 5600.0)
# (5, 'Rust', 899.0)
# (6, 'Angular', 1899.0)
# (7, 'JS', 1999.0)
# (8, 'Pandas', 199.0)
# Baza zostałą zamknięta

# sqlite> INSERT INTO hardware (id,name,price) VALUES (1, 'Samsung',1999);
# sqlite>
# Baza zostałą podłączona
# (1, 'Samsung', 1999.0)
# Baza zostałą zamknięta
