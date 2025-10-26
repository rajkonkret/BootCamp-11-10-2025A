# pętla - możliwość wykonywania tego samego fragmentu kodu wielokrotnie
# for - pętla iteracyjna
import random
from itertools import zip_longest

for i in range(10):  # od 0 do 9
    print(i)

for i in range(10):
    print(i, i, sep=":")  # 9:9
    print(i, i)  # string inserted between values, default a space, 9 9

for i in range(10):
    print(i, end="")  # 0123456789, standardowo: end='\n'

print("Nowa linia")  # 0123456789Nowa linia
print("Prawdziwa nowa linia")
# 0123456789Nowa linia
# Prawdziwa nowa linia
print()

for i in range(1, 20):  # od 1 do 19
    print(i)

for i in range(5):
    print("Komunikat")

for _ in range(1, 5):  # nie ma zmienna
    print("Komunikat")
    # print(_)
    # Komunikat
    # 4

my_string = "Radek"
for i in my_string:  # iteracja po kolekcji, działa, aż dojdzie do ostatniego elementu
    print(i)

for i in range(len(my_string)):
    print(my_string[i])

print(30 * "-")
# Przrobić lotto na pętle
# liczby zapisac w lista_wynik
lista_kule = list(range(1, 50))  # od 1 do 49
lista_wynik = []
for _ in range(6):  # 0 do 5
    wyn = random.choice(lista_kule)
    # print(wyn)
    lista_kule.remove(wyn)
    lista_wynik.append(wyn)

lista_wynik.sort()
print(f"Wylosowane lzby: {lista_wynik}")
# Wylosowane liczby: [9, 3, 38, 48, 13, 19]
# posortowane: 2, 28, 30, 32, 34, 38]

for i in range(10):
    if i % 2 == 0:  # % modulo, reszta z dzielenia
        print(i, "parzysta")
# 0 parzysta
# 2 parzysta
# 4 parzysta
# 6 parzysta
# 8 parzysta

# list comprehensions
lista3 = [j for j in range(1, 10) if j % 2 == 0]
print(lista3)  # [2, 4, 6, 8]

for c in lista3:
    if c == 2:
        c += 1
        print("tylko dla c=2")
    print("Przy każdym przejściu pętli", c)
print("Po zakończeniu pętli")
# tylko dla c=2
# Przy każdym przejściu pętli 3
# Przy każdym przejściu pętli 4
# Przy każdym przejściu pętli 6
# Przy każdym przejściu pętli 8
# Po zakończeniu pętli

imiona = ['Radek', 'Tomek', 'Zenek', 'Zbyszek']
for p in imiona:
    print(p)  # Zbyszek

# 0 Radek
for p in imiona:
    print(imiona.index(p), p)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Zbyszek

for i in range(len(imiona)):  # range(4) -> 0 do 3
    print(i, imiona[i])  # odczyt po indeksie
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Zbyszek

# enumerate() - numeruje kolekcje i zwraca indeks i element kolekcji
for i in enumerate(imiona):
    print(i)

# (0, 'Radek') -> krotka
# (1, 'Tomek')
# (2, 'Zenek')
# (3, 'Zbyszek')
a, b = (3, 'Zbyszek')
print(a, b)

for i, o in enumerate(imiona):
    print(i, o)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Zbyszek

for i, o in enumerate(imiona, start=1):  # numeruje od 1
    print(i, o)
    # 1 Radek
    # 2 Tomek
    # 3 Zenek
    # 4 Zbyszek
# https://www.hackerrank.com/auth/signup
# https://pl.altapps.net/soft/hackerrank-com
# https://www.w3schools.com/python/
# https://naukapythona.com.pl/

ludzie = ["Janek", "Radek", "Tomek", "Marek"]
wiek = [45, 40, 18, 23]

# Radek 40
for i in range(len(ludzie)):
    print(ludzie[i], wiek[i])
# Janek 45
# Radek 40
# Tomek 18
# Marek 23

ludzie = ["Janek", "Radek", "Tomek", "Marek", "Ania"]
wiek = [45, 40, 18, 23]
# for i in range(len(ludzie)):
#     print(ludzie[i], wiek[i])  # IndexError: list index out of range

# zip() - łączy kolekcje
for i in zip(ludzie, wiek):
    print(i)
# ('Janek', 45)
# ('Radek', 40)
# ('Tomek', 18)
# ('Marek', 23)

for l, w in zip(ludzie, wiek):
    print(l, w)
# Janek 45
# Radek 40
# Tomek 18
# Marek 23

# 0 Radek 40

for i in enumerate(zip(ludzie, wiek)):
    print(i)
# (0, ('Janek', 45))
# (1, ('Radek', 40))
# (2, ('Tomek', 18))
# (3, ('Marek', 23))
a, b = (0, ('Janek', 45))
print(a, b)
# 0 ('Janek', 45)
c, d = ('Janek', 45)
print(c, d)  # Janek 45
a, (c, d) = (0, ('Janek', 45))
print(a, c, d)  # 0 Janek 45

for i, (l, w) in enumerate(zip(ludzie, wiek)):
    print(i, l, w)
# 0 Janek 45
# 1 Radek 40
# 2 Tomek 18
# 3 Marek 23
for i, (l, w) in enumerate(zip(ludzie, wiek)):
    print(f"Numer: {i}, Imię: {l}, Wiek: {w}")
# Numer: 0, Imię: Janek, Wiek: 45
# Numer: 1, Imię: Radek, Wiek: 40
# Numer: 2, Imię: Tomek, Wiek: 18
# Numer: 3, Imię: Marek, Wiek: 23

zipped = zip_longest(ludzie, wiek, fillvalue=None)
print(zipped) #<itertools.zip_longest object at 0x100b2fe70>, iterator
# pozwala sekwencyjne odczytywac dane, oszczedzanie zużycia pamięci
zipped_tuple = tuple(zipped) # dane z iteratira zostały zużyte
for i in zipped:
    print(i)
# ('Janek', 45)
# ('Radek', 40)
# ('Tomek', 18)
# ('Marek', 23)
# ('Ania', None)

print(30 * "-")
for o, w in zipped:
    print(o, w)

print(35 * "-")
for o, w in zipped_tuple:
    print(o, w)
# ------------------------------
# -----------------------------------
# Janek 45
# Radek 40
# Tomek 18
# Marek 23
# Ania None