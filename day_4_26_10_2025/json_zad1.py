# json - typ danych para klucz-wartość
# {"name":"John", "age":30, "car":null}
# podwójne cudzysłowia
# None -> null
# wykorzystywany w plikach konfiguracyjnych
# wykorzystywany do komunikacji między systemami
# odpowiednikiem jsona w pythonie jest słownik
import json

person_dict = {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(person_dict)  # <class 'dict'>
print(type(person_dict))  # {'name': 'Radek', 'age': 40, 'czy_pali': None}

with open('nasze_dane.json', "w") as f:
    json.dump(person_dict, f)
# {"name": "Radek", "age": 40, "czy_pali": null}

# beautify - upiiększanie
with open('nasze_dane_b.json', "w") as f:
    json.dump(person_dict, f, indent=4)
# {
#     "name": "Radek",
#     "age": 40,
#     "czy_pali": null
# }

# posortowanie po kluczach
with open('nasze_dane_sort.json', "w") as f:
    json.dump(person_dict, f, indent=4, sort_keys=True)
# {
#     "age": 40,
#     "czy_pali": null,
#     "name": "Radek"
# }
