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

# id,imie,nazwisko,wiek,miasto

# usuniecie i sprzatniecie danych
# sqlite> delete from persons;
# Parse error: no such table: persons
# sqlite> delete from person;
# sqlite> .tables
# ege     person
# sqlite> vacuum;

# usunięcie tabeli
# sqlite> drop table if exists person;
# sqlite> .tables
# ege
# sqlite>

# .mode csv - tryb csv
# import danych z pliku csv
# sqlite> .import dane_person.csv person
# sqlite> .tables
# person
# sqlite>

#  select * from person where wiek > 60;
#  select * from person where wiek < 25;
# select * from person where wiek BETWEEN 30 AND 40;
# sqlite> select * from person WHERE miasto='Lublin';
# 69|Inga|Sajda|61|Lublin
# 80|Aniela|Tomalak|24|Lublin
# sqlite>

# select * from person WHERE miasto!='Warszawa';
#  select * from person order by nazwisko DESC;

# sqlite> select avg(wiek) as srednia_wiek from person;
# 42.04
# sqlite>

# sqlite> select count(*) as liczba_osob from person;
# 100

# unikalne wartości - liczba
# sqlite> select count(DISTINCT miasto) as liczba_miast from person;
# 79

# srednia wieku dla każdego miasta
# sqlite> select miasto, avg(wiek) as srednia from person group by miasto;
# Biała Podlaska|49.0
# Białystok|23.0
# Bielsko-Biała|36.5
# Biłgoraj|37.0
# Bochnia|42.0

# ile osób w danym miescie
# sqlite> select miasto, count(*) as liczba from person group by miasto order by liczba DESC;
# Olkusz|3
# Gniezno|3
# Ząbki|2
# Tychy|2

# zaokrąglone
# sqlite> select  miasto, round(avg(wiek),2) as srednia from person group by miasto;
# Biała Podlaska|49.0

# miasta gdzie srednia wieku > 50
# sqlite> select miasto from person  group by miasto having avg(wiek) > 50;
# Chorzów
# Cieszyn
# Dzierżoniów

# imiona zaczynające się na literę S
# sqlite> select * from person where imie LIKE 'S%';
# 7|Sylwia|Lipowicz|67|Wejherowo
# 28|Szymon|Piestrzeniewicz|66|Cieszyn
# 52|Sonia|Maciejuk|56|Lubartów
# 59|Szymon|Niemira|62|Malbork
# 78|Sebastian|Pyć|19|Kędzierzyn-Koźle
# sqlite>

# sqlite> select * from person where imie LIKE 'S%';
# 7|Sylwia|Lipowicz|67|Wejherowo
# 28|Szymon|Piestrzeniewicz|66|Cieszyn
# 52|Sonia|Maciejuk|56|Lubartów
# 59|Szymon|Niemira|62|Malbork

# sqlite> select * from person where miasto like 'p%';
# 34|Liwia|Barłóg|37|Płock
# 53|Tola|Chojak|51|Puławy
# 58|Robert|Kopciuch|33|Pabianice
# 71|Maciej|Męcik|37|Poznań
# 86|Marianna|Rutowicz|18|Płońsk

# wskazanie kolumn
# sqlite> select imie, wiek from person;
# Fabian|58
# Marcin|54
# Wiktor|31
# Aniela|43

# 5 najstarszych osob
# sqlite> select * from person order by wiek DESC LIMIT 5;
# 6|Monika|Szkoda|70|Tychy
# 13|Nicole|Grzywnowicz|70|Tczew
# 65|Ida|Pleskot|70|Kętrzyn
# 15|Antoni|Wiekiera|68|Jaworzno
# 18|Kacper|Kuban|68|Lubin
# sqlite>

# najmłodsze osoby z Lublina, limit 5
# select * from person where miasto='Lublin' order by wiek ASC LIMIT 5;