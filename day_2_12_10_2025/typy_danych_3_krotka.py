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

print(tupla_liczby)  # (43, 55, 22.34, 11, 200)

# slicowanie tupli
print(tupla_liczby[:3])  # (43, 55, 22.34)
print(tupla_liczby[0:3])  # (43, 55, 22.34)
print(tupla_liczby[1:3])  # (55, 22.34)
print(tupla_liczby[2:])  # (22.34, 11, 200)

print(tupla_liczby[-1])  # 200
print(tupla_liczby[::-1])  # (200, 11, 22.34, 55, 43)
print(tupla_liczby[-1::-1])  # (200, 11, 22.34, 55, 43)
# [start:stop:krok] krok -1 oznacza krok wstecz
print(tupla_liczby[1:4:2])  # (55, 11)
print(tupla_liczby[:])  # (43, 55, 22.34, 11, 200) - cała tupla w normalnej kolejności

print(tupla_names)  # ('Radek', 'tomek', 'Zenek', 'Bartek')
# sprawdzenie czy element istnieje w krotce
print("Radek" in tupla_names)  # True oznacza, że element jest w kolekcji

# count() - zlicza ile razy eleemnt wystąpi w tupli (krotka)
print(tupla_names.count("tomek"))  # występuje 1 raz

# index() - sprawdzenie na którym indeksie znajduje się element
print(tupla_names.index("Radek"))  # index numer 0

# sorted() - sortowanie kolekcji
# zwrócił listę posortowaną
print(sorted(tupla_names))
# ['Bartek', 'Radek', 'Zenek', 'tomek']
# nie zmienił oryginalnej tupli!!!
print(tupla_names)  # ('Radek', 'tomek', 'Zenek', 'Bartek')

# sortowanie z odwróćeniem
print(sorted(tupla_names, reverse=True))  # zwraa listę!!!
# ['tomek', 'Zenek', 'Radek', 'Bartek']

# nie zmienia krotki
print(tupla_names)  # ('Radek', 'tomek', 'Zenek', 'Bartek')

# rozpakowanie tupli
a, b = 1, 2  # wg kolejności trafia do zmiennych
print(f"{a=}, {b=}")  # a=1, b=2

# zamiana wartości zmiennych miedzy sobą
b, a = a, b
print(f"{a=}, {b=}")  # a=2, b=1

print(type((1, 2)))  # <class 'tuple'>

tup1 = 1, 2
print(type(tup1))  # <class 'tuple'>

a, b = tup1
print(f"{a=}, {b=}")
# a=1, b=2

tup2 = 1, 2, 3
print(type(tup2))  # <class 'tuple'>
# a, b = tup2  # ValueError: too many values to unpack (expected 2)
# zwykła zmienna przyjmuje jeden element
a, *b = tup2  # * worek na pozostałe dane
print(f'{a=}, {b=}')  # a=1, b=[2, 3]

print(tupla_names)  # ('Radek', 'tomek', 'Zenek', 'Bartek')
# name1, name2, name3
# rozpakować tupla_names na trzy zmienne
