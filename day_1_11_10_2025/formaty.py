user = "Tomek"  # str
wiek = 41  # int
wersja = 3.900001
print(type(wersja))  # <class 'float'>, zmiennoprzecikowe
liczba = 890789678567456  # int

# ten sposób typy są sprawdzane
print("Witaj %s masz teraz %d lat." % (user, wiek))  # Witaj Tomek masz teraz 41 lat.
# print("Witaj %s masz teraz %d lat." % (wiek, user)) # TypeError: %d format: a real number is required, not str
# print("Witaj %d masz teraz %s lat." % (user, wiek)) # TypeError: %d format: a real number is required, not str
# %d: formatowanie liczb całkowitych
# %f: formatowanie liczb zmiennoprzecinkowych
# %s - łańcuch znaków (string)

print("Witaj %(user)s, masz teraz %(wiek)d lat." % {'user': user, "wiek": wiek})
# Witaj Tomek, masz teraz 41 lat.
print("Witaj %(user)s, masz teraz %(age)d lat." % {'user': user, "age": wiek})
# Witaj Tomek, masz teraz 41 lat.
print("Witaj %(user)s, masz teraz %(age)d lat, miło cię widzieć %(user)s" % {'user': user, "age": wiek})
# Witaj Tomek, masz teraz 41 lat, miło cię widzieć Tomek

# zrobić za pomocą f-string
print(f"Witaj {user}, masz teraz {wiek} lat, miło cię widzieć {user}.")
# Witaj Tomek, masz teraz 41 lat, miło cię widzieć Tomek.

# nie sprawdza typów
print(f"Witaj {wiek}, masz teraz {wiek} lat, miło cię widzieć {user}.")
# Witaj 41, masz teraz 41 lat, miło cię widzieć Tomek.

print("Używamy wersji Pythona %i" % 3)  # Używamy wersji Pythona 3
print("Używamy wersji Pythona %f" % 3)  # Używamy wersji Pythona 3.000000
print("Używamy wersji Pythona %f" % 3.9)  # Używamy wersji Pythona 3.900000
print("Używamy wersji Pythona %.2f" % 3.9)  # Używamy wersji Pythona 3.90
print("Używamy wersji Pythona %.1f" % 3.9)  # Używamy wersji Pythona 3.9
print("Używamy wersji Pythona %.0f" % 3.9)  # Używamy wersji Pythona 4 - zaokrągli przy wyświetleniu
print("Używamy wersji Pythona %.f" % 3.9)  # Używamy wersji Pythona 4 - zaokrągli przy wyświetleniu

x = 3.99
print("Liczba: %.f" % x)  # Liczba: 4
print("Liczba się nie zmieniła:", x)  # Liczba się nie zmieniła: 3.99

# zaokrąglenie wartości liczby
x = round(x)
print("Liczba po zaokrągleniu:", x)  # Liczba po zaokrągleniu: 4

x = 3.14157890
x = round(x, 2)
print("liczba zaokrąglona do dwóch miejsc po przecinku:", x)
# liczba zaokrąglona do dwóch miejsc po przecinku: 3.14

print(f"Używamy wersji pythona {wersja}")  # Używamy wersji pythona 3.900001
print(f"Używamy wersji pythona {wersja:.1f}")  # Używamy wersji pythona 3.9
print(f"Używamy wersji pythona {wersja:.2f}")  # Używamy wersji pythona 3.90
print(f"Używamy wersji pythona {wersja:.0f}")  # Używamy wersji pythona 4
# print(f"Używamy wersji pythona {wersja:.f}")  # ValueError: Format specifier missing precision

print(liczba)  # 890789678567456
print(f"Nasza duża liczba: {liczba:,}")  # Nasza duża liczba: 890,789,678,567,456
print(f"Nasza duża liczba: {liczba:_}")  # Nasza duża liczba: 890_789_678_567_456

# zamiana na spacje, kropkę
print(f"Nasza duża liczba: {liczba:,}".replace(",", "."))  # Nasza duża liczba: 890.789.678.567.456
print(f"Nasza duża liczba: {liczba:_}".replace("_", " "))  # Nasza duża liczba: 890 789 678 567 456


