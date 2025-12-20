# docker -v  - wersja dockera
#  docker ps - lista aktywnych kontenerów
# docker ps -a  - lista wszystkich kontenerów (aktywnych i nieaktywnych)

# docker run --name my-postgres1 -e POSTGRES_USER=myuser -e POSTGRES_PASSWORD=mypassword -e POSTGRES_DB=mydatabase -p 5432:5432 -d postgres
# psql -U myuser -d mydatabase -h localhost -p 5432 - logowanie do bazy mydatabase w kontenerze

#  docker stop my-postgres1 - zatrzymanie kontenera o nazwie my-postgres1
# docker start my-postgres1 - uruchomienie kontenera o nazwie my-postgres1

# pgAdmn - program do zarządzania bazą postgres
# localhost - 127.0.0.1
import psycopg2

# pip install psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="mydatabase",
    user="myuser",
    password="mypassword"
)

cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users(id SERIAL PRIMARY KEY, name TEXT);")
conn.commit()

cursor.close()
conn.close()