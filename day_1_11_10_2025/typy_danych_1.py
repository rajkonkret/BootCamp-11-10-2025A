wiek = 47  # int
rok = 2025  # int
temp = 36.6  # float

print(temp)  # 36.6
print(type(temp))  # <class 'float'>

print(wiek + rok)  # 2072
print(wiek - rok)  # -1978
print(wiek * rok)  # 95175

print(wiek / rok)  # 0.023209876543209877 -> float
print(rok // wiek)  # 43, część całkowita z dzielenia
print(10 // 3)  # 3

print(rok % wiek)  # modulo, reszta z dzielenia
print(10 % 3)  # reszta 1,  3 * 3 + 1 = 10

wynik = wiek ** rok  # potęgowanie
print(wynik)
print(f"Wiek do potęgi rok: {wynik:,}")

# sprawdzenie długosci liczby
# print(f"Długość: {len(wynik)}") # TypeError: object of type 'int' has no len()
print(f"Długość: {len(str(wynik))}")  # Długość: 3386

# print(wynik ** 2)
# ValueError: Exceeds the limit (4300 digits) for integer string conversion;
# use sys.set_int_max_str_digits() to increase the limit

print(74 - 8 * 45 + 8 / 2 + 8 / 2)  # -278.0
print(74 - (8 * 45) + 8 / 2 + 8 / 2)  # -278.0
print(74 - (8 * 45) + (8 / 2 + 8) / 2)  # -280.0
