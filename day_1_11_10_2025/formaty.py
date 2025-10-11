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