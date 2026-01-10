# Redis (Remote Dictionary Server) to superszybki,
# otwartoźródłowy magazyn danych działający w pamięci RAM (in-memory),
# który przechowuje dane w formacie klucz-wartość,
# ale obsługuje też złożone struktury (listy, hasze, zestawy, JSON),
# używany głównie jako baza danych, cache aplikacji lub broker wiadomości,
# zapewniając niezwykłą wydajność dzięki przechowywaniu danych w RAM

# docker pull redis
# docker run --name redis-server -d -p 6379:6379 redis

import redis

# pip install redis

# połączenie do bazy Reddis, localhost, port 6379
r = redis.Redis()

# dodanie klucza i wartości
r.set('name', "Radek")

# odczytanie wartości dla klucza
wartosc = r.get('name')
print(wartosc)  # b'Radek' - dostalismy bajty
print(type(wartosc))  # <class 'bytes'>
print(wartosc.decode('utf-8'))  # Radek
