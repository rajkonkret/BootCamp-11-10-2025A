user = "Tomek"  # str
wiek = 41  # int
wersja = 3.900001
print(type(wersja))  # <class 'float'>, zmiennoprzecikowe
liczba = 890789678567456  # int

print("Witaj %s masz teraz %d lat." % (user, wiek))  # Witaj Tomek masz teraz 41 lat.
# print("Witaj %s masz teraz %d lat." % (wiek, user)) # TypeError: %d format: a real number is required, not str
# print("Witaj %d masz teraz %s lat." % (user, wiek)) # TypeError: %d format: a real number is required, not str
# %d: formatowanie liczb całkowitych
# %f: formatowanie liczb zmiennoprzecinkowych
# %s - łańcuch znaków (string)


