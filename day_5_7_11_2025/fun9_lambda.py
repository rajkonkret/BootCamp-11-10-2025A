# funkcja lambda
# skrocony zapis funkcji
# lambda zwraca wynik - return
# funkcja anonimowa - wykonanie w miejscu deklaracji
from day_3_25_10_2025.petle import lista_wynik

odejmij = lambda a, b: a - b
print(odejmij(6, 8))  # -2
print(odejmij(b=6, a=8))  # 2

addition = lambda a, b: a + b
print(addition(6, 9))  # 15
res = addition(23, 89)
print(f"wynik dodawania: {res}")  # wynik dodawania: 112

res = lambda *args: sum(args)
print(res(10, 20))  # 30

# suma argumentów nazwanych, sumujemy wartości
res = lambda **kwargs: sum(kwargs.values())
# {a:10, b:20}
print(res(a=10, b=20))  # 30

product = lambda a, b: a * b
print(product(4, 5))  # 20


def product1(nums):
    total = 1
    for i in nums:
        total *= i
    return total


res1 = lambda **kwargs: product1(kwargs.values())
print(res1(a=10, b=90))  # 900


def my_func(n):
    return lambda a: a + n  # zwracamy funkcje (adres)


add10 = my_func(10)  # 15
add20 = my_func(20)  # 25
add30 = my_func(30)  # 35

print(add10(5))
print(add20(5))
print(add30(5))

# oblicz_vat -> lambda
oblicz_vat = lambda cena, vat=8: cena * (100 + vat) / 100
print(oblicz_vat(1000))  # 1080.0
print(oblicz_vat(1000, 23))  # 1230.0
print(oblicz_vat(vat=15, cena=1000))  # 1150.0

wiek = lambda x: "dziecko" if x < 10 else ('nastolatek' if x < 18 else "dorosły")
print(wiek(9))  # dziecko
print(wiek(10))  # nastolatek
print(wiek(17))  # nastolatek
print(wiek(18))  # dorosły
print(wiek(50))  # dorosły

# mapowanie danych
lista = [1, 2, 3, 45, 67, 78, 100, 200, 300]

# stworzyc nową listę z wartości * 2
lista_wyn = []
for i in lista:
    lista_wyn.append(i * 2)
print(lista_wyn)
# [2, 4, 6, 90, 134, 156, 200, 400, 600]

print([i * 2 for i in lista])


# [2, 4, 6, 90, 134, 156, 200, 400, 600]

# print(lista * 2)
# [1, 2, 3, 45, 67, 78, 100, 200, 300, 1, 2, 3, 45, 67, 78, 100, 200, 300]

def zmien(x):
    return x * 2


lista_wynikyn_f = []
for i in lista:
    lista_wynikyn_f.append(zmien(i))
print(lista_wynikyn_f)
# [2, 4, 6, 90, 134, 156, 200, 400, 600]

# funkcja wyższego rzędu - przyjmuje inną funkcje jako argument
# map() - mapowanie, zmienia dane wg zadanej funkcji
print(f"Zastosowannie map(): {list(map(zmien, lista))}")
# Zastosowannie map(): [2, 4, 6, 90, 134, 156, 200, 400, 600]

# Lambda jako funkcja anonimowa - nie jest przypisana do zmiennej
# możliwośc użycia w miejscu deklaracji
print(f"Zastosowannie map(): {list(map(lambda x: x * 2, lista))}")
# Zastosowannie map(): [2, 4, 6, 90, 134, 156, 200, 400, 600]
print(f"Zastosowannie map(): {list(map(lambda x: x * 3, lista))}")
# Zastosowannie map(): [3, 6, 9, 135, 201, 234, 300, 600, 900]
print(f"Zastosowannie map(): {list(map(lambda x: x * 12, lista))}")
print(f"Zastosowannie map(): {list(map(lambda x: x * 1.1, lista))}")
# Zastosowannie map(): [12, 24, 36, 540, 804, 936, 1200, 2400, 3600]
# Zastosowannie map(): [1.1, 2.2, 3.3000000000000003, 49.50000000000001,
# 73.7, 85.80000000000001, 110.00000000000001, 220.00000000000003, 330.0]

# filtrowanie danych

liczby_parzyste = []
for i in lista:
    if i % 2 == 0:  # % - modulo - reszta z dzielenia
        liczby_parzyste.append(i)
print(liczby_parzyste)
