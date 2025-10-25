# pętla - możliwość wykonywania tego samego fragmentu kodu wielokrotnie
# for - pętla iteracyjna
import random

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

for i, o in enumerate(imiona, start=1):
    print(i, o)
    # 1 Radek
    # 2 Tomek
    # 3 Zenek
    # 4 Zbyszek
# https://www.hackerrank.com/auth/signup
# https://pl.altapps.net/soft/hackerrank-com
# https://www.w3schools.com/python/
