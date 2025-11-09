# funkcje - wydzielony fragment kodu, możemy wykonac w dowolnym momencie
# funkcja przed użyciem musi zostac zdefiniowana
# w miejscu definicji funkcja się nie wykona
# aby funkcja się uruchomiła musimy ją wywołąć

# zmienne globalne
# dostępne wewnątrz funkcji
a = 6
b = 8


# te funkcje nie zwracają wyniku
# deklaracja funkcji
# PEP8 zaleca by funkcja była oddzielona dwoma liniami od reszty progrmau
def dodaj():  # funkcja bezargumentowa
    print(a + b)
    c = 7  # zmienna loklna, widocznośc tylko wewnatrz funkcji


# dwa obowiązkowe argumenty
def dodaj2(a, b):
    # a i b o zasięgu lokalanym
    print(a + b)


# argumetnty funkcji z domyslna wartością, c=0
# pozwala zasymulować przeciążanie funkcji liczbą argumentó∑
def odejmij(a, b, c=0):
    print(a - b - c)


# wywołanie funkcji
print(dodaj)  # <function dodaj at 0x105ae19e0>
print(type(dodaj))  # <class 'function'>
# nazwa funkcji i () - uruchomienie funkcji
dodaj()  # 14
# print(c)

# dodaj2()  # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
dodaj2(5, 9)  # 14, obowiązkowo dwa parametry do przekazania

odejmij(1, 2)  # -1, c=0
odejmij(1, 2, 3)  # -4, c=3

# argumenty przekazane po pozycji
odejmij(1, 2)
dodaj2(3, 4)  # 7

# argumenty przekazane po nazwie
odejmij(c=9, b=90, a=87)  # -12
odejmij(b=90, a=12)  # -78

# mieszane
odejmij(1, 2, c=9)  # -10
odejmij(1, b=2, c=9)  # -10
odejmij(1, c=2, b=9)  # -10

# argumnty pozycyjne muszą byc przekazywane przed argumentami nazwanymi
# SyntaxError: positional argument follows keyword argument
# odejmij(c=90, 1, 2)

print(10 * "-")
print(dodaj())
# 14
# None

# TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
# print(dodaj() + dodaj2(5, 90))
# funkcja nie zwraca wyniku, nie możemy go użyc
