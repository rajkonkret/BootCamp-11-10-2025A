# funkcja lambda
# skrocony zapis funkcji
# lambda zwraca wynik - return
# funkcja anonimowa - wykonanie w miejscu deklaracji

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
