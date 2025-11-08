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
