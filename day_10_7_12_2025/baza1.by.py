# sqlite3 --version
#  sqlite3 test.db - utworzenie/otworzenie bazy danch

# tworzenie tabeli
# create table users (id INT PRIMARY KEY, name VARCHAR(100), age iNT);

# sprawdzenie i wypisanie dostepnych tabel
# .tables

# sqlite> .tables
# users
# sqlite>

# dodanie rekordu
#  insert into users (id,name,age) values (1,'Jan kowalski', 30);

# odzczyt rekordów
# select * from users;

# zmian awartości
#  update users set age=31 where id=1;

# sqlite> select * from users;
# 1|Jan kowalski|31

# usunięcie rekordu
# delete from users where id=1;

# -----
# sqlite> insert into users (id,name,age) values (1,'Jan kowalski', 30);
# sqlite> insert into users (id,name,age) values (2,'Radek Nowak', 35);
# sqlite> insert into users (id,name,age) values (3,'Anna Palec', 28);

# rosnąco po wieku
# sqlite> select * from users order by age;
# 3|Anna Palec|28
# 1|Jan kowalski|30
# 2|Radek Nowak|35

# malejąco
# qlite> select * from users order by age desc;
# 2|Radek Nowak|35
# 1|Jan kowalski|30
# 3|Anna Palec|28

# wypisze osoby o wieku > 29
# sqlite> select * from users where age > 29;
# 1|Jan kowalski|30
# 2|Radek Nowak|35
# sqlite>

# zmiananazwy tabeli
# sqlite> alter table users rename to ege;
# sqlite> .tables
# ege
# sqlite>
