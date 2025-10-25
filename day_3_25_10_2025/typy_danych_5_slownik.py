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
