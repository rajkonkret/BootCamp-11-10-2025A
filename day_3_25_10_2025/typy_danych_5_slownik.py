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
