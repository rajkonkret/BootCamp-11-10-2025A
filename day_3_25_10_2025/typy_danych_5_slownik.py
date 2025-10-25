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
