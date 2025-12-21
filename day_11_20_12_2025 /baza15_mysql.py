import mysql.connector
from mysql.connector import Error

# tableplus, phpMyAdmin, Adminer - gui do mysql
# mariadb  - fork bazy mysql

# pip install mysql-connector-python

# docker run -d \
#   --name mysql_db1 \
#   -e MYSQL_ROOT_PASSWORD=abc123 \
#   -e MYSQL_DATABASE=baza \
#   -p 3306:3306 \
#   mysql:8.0

# docker run -d --name mysql_db1 -e MYSQL_ROOT_PASSWORD=abc123 -e MYSQL_DATABASE=baza -p 3306:3306 mysql:8.0
try:
    connection = mysql.connector.connect(
        host="localhost",
        port=3306,  # standartowy port dla mysql
        database="baza",
        user="root",
        password="abc123"
    )

    if connection.is_connected():
        db_info = connection.server_info
        print("Połączenie z serwerem MySql w wersji:", db_info)

        cursor = connection.cursor()
        cursor.execute("select database();")

        record = cursor.fetchone()
        print("Połaczenie z bazą danych:", record)

except Error as e:
    print("Bład podczas połączenia do bazy danych MySql:", e)

finally:
    if connection.is_connected():
        connection.close()
        print("Połączenie z MySQL zostało zamknięte")
# Połączenie z serwerem MySql w wersji: 8.0.42
# Połaczenie z bazą danych: ('baza',)
# Połączenie z MySQL zostało zamknięte
