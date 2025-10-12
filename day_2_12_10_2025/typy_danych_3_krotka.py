# krotka (tupla) - kolekcja do odczytu, niemutowalna
# lepsze wykorzystanie pamięci
# przechowywanie konfiguracji
# jednoelemntowa krotka często jest traktowana jako stała - wypełnia zmnamiona zmiennej

tupla1 = "Radek"
print(type(tupla1))  # <class 'str'>

tupla2 = ("Radek")
print(type(tupla2))  # <class 'str'>

# PEP8 zaleca tworzenie tupli jedoelementowej z nawiasami ()
# czytelnijszy zapis
tupla3 = ("Radek",)
print(type(tupla3))  # <class 'tuple'>
print(tupla3)  # ('Radek',)

tupla4 = "Radek",
print(type(tupla4))  # <class 'tuple'>
print(tupla4)  # ('Radek',)

tupla_names = "Radek", "tomek", "Zenek", "Bartek"
print(type(tupla_names))  # <class 'tuple'>
print(tupla_names)  # ('Radek', 'tomek', 'Zenek', 'Bartek')

temp = 36, 6
print(type(temp))  # <class 'tuple'>
print(temp)  # (36, 6)

# tupla_liczby = 43, 55, 22.34, 11, 200
tupla_liczby = (43, 55, 22.34, 11, 200)
print(tupla_liczby)
print(type(tupla_liczby))
# (43, 55, 22.34, 11, 200)
# <class 'tuple'>

# tupla (krotka) jest niemutowalna - nie można dokonać w niej zmian
# temp[0] = 1  # TypeError: 'tuple' object does not support item assignment

# nie da się usunąć elementu z krotki
# del temp[0]  # TypeError: 'tuple' object doesn't support item deletion

# można usunąć całą krotkę z pamięci
del temp  # <class 'tuple'>
# tupli nie ma. można usunąć
# print(temp)  # NameError: name 'temp' is not defined

print(tupla_liczby)