# funkcje zwracające wynik
# muszą byc zakończone return

def odejmij(a, b):
    return a - b  # return - funkcja zwraca wynik


def odejmij2(a=0, b=0, c=0):
    return a - b - c


# musimy skonsumować wynik
print(odejmij(7, 8))  # -1

wynik = odejmij(6, 9)  # zapis wyniku funkcji do zmmiennej
print("Wynik:", wynik)  # Wynik: -3

print(odejmij2())  # 0                              0
print(odejmij2(5))  # 0                             5
print(odejmij2(5, 6))  # 0                          -1
print(odejmij2(5, 6, 7))  # 0                       -8
print(odejmij2(c=90))  # 0                          -90
print(odejmij2(c=90, a=65))  # 0                    -25
print(odejmij2(c=90, a=65, b=99))  # 0              -124
print(odejmij2(1, c=65, b=99))  # 0                 -163
wynik = odejmij2(7, 9)  #
print("Wynik:", wynik)  # Wynik: -2

print(odejmij2(6, 9) + odejmij(100, 6))  # 91


# nie można użyć funkcji zanim nie zostanie zadeklaroewana
# print(oblicz_vat(1000)) # NameError: name 'oblicz_vat' is not defined
def oblicz_vat(cena, vat=23):
    return cena * (100 + vat) / 100


print(oblicz_vat(1000))  # 1230.0
print(oblicz_vat(1000, 6))  # 1060.0
print(oblicz_vat(vat=15, cena=2000))  # 2300.0 -> float

vat1 = oblicz_vat(1000)
if vat1 == 1230:
    print("poprawnie")
else:
    print("Błąd")
    # poprawnie
