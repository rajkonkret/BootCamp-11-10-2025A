# funkcje - wydzielony fragment kodu, możemy wykonac w dowolnym momencie
# funkcja przed użyciem musi zostac zdefiniowana
# w miejscu definicji funkcja się nie wykona
# aby funkcja się uruchomiła musimy ją wywołąć

# zmienne globalne
# dostępne wewnątrz funkcji
a = 6
b = 8


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
