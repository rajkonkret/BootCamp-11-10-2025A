# liczby float, zmiennoprzecinkowe
# błąd zaokrąglenia
print(0.2 + 0.8)  # 1.0
print(0.2 + 0.7)  # 0.8999999999999999
print(0.1 + 0.2)  # 0.30000000000000004
# zapamiętane w postaci wykłądnizej
# # x=SMB^E
# #  S (ang. sign) – znak liczby, 1 lub −1,
# #  M (ang. mantissa) – znormalizowana mantysa, liczba ułamkowa[1],
# #  B (ang. base) – podstawa systemu liczbowego[1] (2 dla systemów komputerowych),
# #  E (ang. exponent) – wykładnik, cecha, liczba całkowita[1].
# przechowujemy najbliższe przybliżennie
# For example, in a floating-point arithmetic with five base-ten digits,
# the sum 12.345 + 1.0001 = 13.3451 might be rounded to 13.345.

# decimal - pozwala ominąc błąd zaokrąglenia
from decimal import Decimal

# tworzenie liczb
decimal1 = Decimal("0.1")
decimal2 = Decimal(0.1)
decimal3 = Decimal(1)

# wypisanie
print(decimal1)  # 0.1
print(decimal2)  # 0.1000000000000000055511151231257827021181583404541015625
print(decimal3)  # 1

# porównanie decimali
print(f"{decimal1 == decimal2 = }")  # decimal1 == decimal2 = False
print(f"{decimal1 == Decimal("0.1") = }")  # decimal1 == Decimal("0.1") = True
print(f"Decimal(1) == Decimal(1) {decimal3 == Decimal("1")}")  # Decimal(1) == Decimal(1) True

# operacje matematyczne
a = Decimal("10.345")
b = Decimal("3.2")

add = a + b
print("Dodawanie:", a)  # Dodawanie: 10.345

substract = a - b
multiply = a * b
divide = a / b

print("Odejmowanie:", substract)  # Odejmowanie: 7.145
print("Mnożenie:", multiply)  # Mnożenie: 33.1040
print("Dzielenie:", divide)  # Dzielenie: 3.2328125

precyzja = Decimal("0.01")
print("Liczby zaokrąglone do dwóch miejsc po przecinku:")
add = add.quantize(precyzja)
substract = substract.quantize(precyzja)
multiply = multiply.quantize(precyzja)
divide = divide.quantize(precyzja)

print("Dodawanie:", a)  # Dodawanie: 10.345
print("Odejmowanie:", substract)  # Odejmowanie: 7.14
print("Mnożenie:", multiply)  # Mnożenie: 33.10
print("Dzielenie:", divide)  # Dzielenie: 3.23
