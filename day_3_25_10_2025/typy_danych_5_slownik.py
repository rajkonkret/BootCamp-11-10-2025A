# słownik - para klucz - wartość
# {'klucz' : 'wartosc'}
# ctrl / - szybki komentarz
# odpowiednik jsona - {"name":"John", "age":30, "car":null}
# klucze w słowniku  nie mogą się powtarzać

my_dict = {"A": "one", "B": "two", "C": "three", "D": "four"}
print(my_dict)  # {'A': 'one', 'B': 'two', 'C': 'three', 'D': 'four'}
# ctrl alt l - formatowanie wg PEP8

# tworzenie pustego słownika
empty_dict = dict()
print(type(empty_dict))  # sprawdzenie typu, <class 'dict'>
print(empty_dict)  # {} - pusty słownik

empty_dict_2 = {}
print(type(empty_dict_2))  # <class 'dict'>
print(empty_dict_2)  # {} - pusty słownik

data_with_integer = {1: "one", 2: "two", 3: "three"}
print(data_with_integer)  # {1: 'one', 2: 'two', 3: 'three'}

# klucze mieszane
dict_mixed = {1: "one", 2: "two", "A": "three"}
print(dict_mixed)  # {1: 'one', 2: 'two', 'A': 'three'}

# klucz, wartość, para
print(dict_mixed.keys())  # dict_keys([1, 2, 'A']) # - klucze
print(dict_mixed.values())  # dict_values(['one', 'two', 'three']) - wartości
print(dict_mixed.items())  # dict_items([(1, 'one'), (2, 'two'), ('A', 'three')]) - pary

print(data_with_integer.keys())  # dict_keys([1, 2, 3]) - lista kluczy

dict_with_list = {1: "one", 2: "two", "A": ["arek", 'jhon', 'maria']}
print(dict_with_list)  # {1: 'one', 2: 'two', 'A': ['arek', 'jhon', 'maria']}

dict_with_list_and_tuple = {
    1: 'one',
    2: 'two',
    "A": ['asif', 'jhon', 'maria'],
    "B": ("bat", 'cat', 'hat')
}
print(dict_with_list_and_tuple)
# {1: 'one', 2: 'two', 'A': ['arek', 'jhon', 'maria']}

dict_with_all = {
    1: 'one',
    2: 'two',
    "A": ['asif', 'jhon', 'maria'],
    "B": ("bat", 'cat', 'hat'),
    "C": {"Name", "age", 10}  # zbiór
}

print(dict_with_all)
# {1: 'one', 2: 'two', 'A': ['asif', 'jhon', 'maria'], 'B': ('bat', 'cat', 'hat'), 'C': {10, 'Name', 'age'}}

dict_with_dict = {
    1: 'one',
    2: 'two',
    "A": ['asif', 'jhon', 'maria'],
    "B": ("bat", 'cat', 'hat'),
    "C": {"Name", "age", 10},  # zbiór,
    "D": {"Name": "Radek", "age": 76}
}
print(dict_with_dict)
# {1: 'one', 2: 'two',
# 'A': ['asif', 'jhon', 'maria'],
# 'B': ('bat', 'cat', 'hat'),
# 'C': {10, 'Name', 'age'},
# 'D': {'Name': 'Radek', 'age': 76}}

# tworzenie słownika z selwencji kluczy
keys = {"a", 'b', "c", "d"}
my_dict_from_keys = dict.fromkeys(keys)
print(my_dict_from_keys)  # {'d': None, 'a': None, 'c': None, 'b': None}
# domyślnie wartośi jako None

value = 10
my_dict_3 = dict.fromkeys(keys, value)
print(my_dict_3)  # {'b': 10, 'c': 10, 'd': 10, 'a': 10}
# jako wartość podstwi wartośc zadaną

value = [10, 20, 30]
my_dict_4 = dict.fromkeys(keys, value)
print(my_dict_4)
# {'d': [10, 20, 30], 'b': [10, 20, 30], 'a': [10, 20, 30], 'c': [10, 20, 30]}

# zastosowanie fromkeys() do usunięcia duplikatów z listy, bez zmiany kolejności
# od python 3.7 kolejnośc w słowniku jest zachowana
keys = [1, 2, 2, 3, 4, 4, 5]
dict_unique = dict.fromkeys(keys)
print(dict_unique)  # {1: None, 2: None, 3: None, 4: None, 5: None}
list_unique = list(dict_unique)
print(list_unique)  # [1, 2, 3, 4, 5], bez zmainy kolejności

print(list(dict.fromkeys(keys)))  # [1, 2, 3, 4, 5]

# wypisanie wartościa dla klucza
print(dict_with_dict["A"])  # ['asif', 'jhon', 'maria']

print(my_dict)  # {'A': 'one', 'B': 'two', 'C': 'three', 'D': 'four'}
print(my_dict['A'])  # one

print(data_with_integer)  # {1: 'one', 2: 'two', 3: 'three'}
print(data_with_integer[1])  # one
print(dict_with_all["C"])  # {'age', 10, 'Name'}

# print(my_dict_4['e'])  # KeyError: 'e'

print(my_dict_4.get('a'))  # [10, 20, 30]
print(my_dict_4.get('e'))  # None, oznacza brak klucza w słowniku
# None - odpowiednik nulla w innych systemach
# mozemy ustawić wartośc domyślną, jaka będzie zwracana gdy nie ma klucza w słowniku
print(my_dict_4.get('e', "Nie ma"))  # Nie ma - gdy brak klucza
print(my_dict_4.get('a', "Nie ma"))  # [10, 20, 30]

# nadpisanie wartoścci dla klucza
my_dict5 = {"Name": "Radek", "ID": 12345, "DDB": 1991, "Address": "Warsaw"}
print(my_dict5)
print(my_dict5['DDB'])  # 1991
print(my_dict5.get("DDB"))  # 1991

my_dict5["DDB"] = '1980'
print(my_dict5)  # {'Name': 'Radek', 'ID': 12345, 'DDB': '1980', 'Address': 'Warsaw'}
print(type(my_dict5['DDB']))  # <class 'str'>

my_dict5["Address"] = "Warsaw Centre"
print(my_dict5)  # {'Name': 'Radek', 'ID': 12345, 'DDB': '1980', 'Address': 'Warsaw Centre'}

dict1 = {"DDB": 1995}
print(dict1)  # {'DDB': 1995}

# update słownika innym słownikiem
# jesli klucz istnieje, wartość zostanie nadpisana
my_dict5.update(dict1)
print(my_dict5)
# {'Name': 'Radek', 'ID': 12345, 'DDB': 1995, 'Address': 'Warsaw Centre'}

dict2 = {'cpi': 3.41}
print(dict2)  # {'cpi': 3.41}

# update słownika
# jesli klucz nie istnieje zostanie dopisany do słownika
my_dict5.update(dict2)
print(my_dict5)
# {'Name': 'Radek', 'ID': 12345, 'DDB': 1995, 'Address': 'Warsaw Centre', 'cpi': 3.41}

# usunięcie elementu ze słownika
print(my_dict5.pop('cpi'))  # 3.41
print(my_dict5)
# {'Name': 'Radek', 'ID': 12345, 'DDB': 1995, 'Address': 'Warsaw Centre'}

# usunięcie ostatniego eleemntu ze słownika
print(my_dict5.popitem())  # ('Address', 'Warsaw Centre')

# usunięcie
del my_dict5['ID']
print(my_dict5)  # {'Name': 'Radek', 'DDB': 1995}

# usunięcie wszystkich elementów ze słownika
my_dict5.clear()
print(my_dict5)  # {}, został pusty słownik

# usnięcie z pamięci
del my_dict5  # słownik juz nie istnieje
# print(my_dict5)  # NameError: name 'my_dict5' is not defined. Did you mean: 'my_dict'?

# zmiana klucza w słowniku
slownik = {"stary_klucz": "wartość"}
slownik['nowy_klucz'] = slownik.pop('stary_klucz')
print(slownik)  # {'nowy_klucz': 'wartość'}

# kopiowanie słownika
my_dict5 = {"Name": "Radek", "ID": 12345, "DDB": 1991, "Address": "Warsaw"}

# kopia referencji
my_dict5_copy_ref = my_dict5
print(id(my_dict5_copy_ref))  # 4340053888
print(id(my_dict5))  # 4340053888

my_dict5_copy = my_dict5.copy()  # kopia eleemntów słownika, nowe id
my_dict5.clear()
print(my_dict5)  # {}
print(my_dict5_copy_ref)  # {}
print(my_dict5_copy)  # {'Name': 'Radek', 'ID': 12345, 'DDB': 1991, 'Address': 'Warsaw'}

print(id(my_dict5_copy_ref))  # 4336744320
print(id(my_dict5))  # 4336744320
print(id(my_dict5_copy))  # 4336744384

dict_small = {"x": 3}
dict_small.update([('y', 3), ("z", 3)])
print(dict_small)  # {'x': 3, 'y': 3, 'z': 3}
print(dict_small.items())  # dict_items([('x', 3), ('y', 3), ('z', 3)])

# input() - pobiera dane od użytkownika
# odp = input("Podaj imię\n")
# print(odp)
# Podaj imięRadek
# Radek
# Podaj imię
# Radek
# Radek

# napisać program, który będzie działał jak słownik angielsko polski

# słownik
# wyswietlic słowka, które potrafi przetłumaczyć
# pobrać dane od użykownika
# wyswietlic tłumaczenie
#
# ang_pol = {"name": "imie", "cat": "kot", "water": "woda"}
# print('-----Słownik ang-pol------')
# print("Mamy takie słówka w słownika:", ang_pol.keys())
# odp = input("Podaj słowko do przetłumaczenia:")
# # print(f"{odp} to {ang_pol[odp]}")
# # print(f"{odp} to {ang_pol.get(odp)}")
# print(f"{odp.strip().lower()} to {ang_pol.get(odp.strip().lower())}")
#
# # ß
# word1 = "GROSS"
# word2 = "groß"
#
# print(word1.lower() == word2.lower())  # False
# """ Return a version of the string suitable for caseless comparisons. """
# # https://www.unicode.org/Public/12.1.0/ucd/CaseFolding.txt
# print(word1.casefold() == word2.casefold())  # True
#
# # dla naszego słownika
# print(f"{odp.strip().casefold()} to {ang_pol.get(odp.strip().casefold())}")
# # Podaj słowko do przetłumaczenia:Cat
# # cat to kot
# # False
# # True
# # cat to kot
# print(f"{odp.strip().casefold()} to {ang_pol.get(odp.strip().casefold(), "Nia mam słówka w słowniku")}")
# # Podaj słowko do przetłumaczenia:Bat
# # bat to None
# # False
# # True
# # bat to None
# # bat to Nia mam słówka w słowniku

# Porgram kalkulator
# pobieramy dwie liczby
# wynik działania (+)
#
# # rzutowanie
# a = input("Podaj lizbę a:")  # -> str
# b = input("Podaj lizbę b:")
# print(a + b)  # konkatenacja, łączenie stringów
# # Podaj lizbę a:5
# # Podaj lizbę b:6
# # 56
#
# a = int(input("Podaj lizbę a:"))  # -> str
# b = float(input("Podaj lizbę b:"))
# print(a + b)
# # Podaj lizbę a:5
# # Podaj lizbę b:6
# # 11.0
# a = int(input("Podaj lizbę a:"))  # -> str
# b = float(input("Podaj lizbę b:"))
# print(int(a) + float(b))
# # Podaj lizbę a:5
# # Podaj lizbę b:6
# # 11.0

print(my_dict5_copy)
# sprawdzenie czy eleemnt istnieje w słowniku
print("Name" in my_dict5_copy)  # True
print("Temat" in my_dict5_copy)  # False

#  Return True if bool(x) is True for all values x in the iterable.
print(all(my_dict5_copy))  # True

# Return True if bool(x) is True for any x in the iterable.
print(any(my_dict5_copy))  # True
