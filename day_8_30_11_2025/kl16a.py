# stworzyc słownik
# zapisać słownik do pliku i odczytac za pomocą pickle
# odczytac wartości klucza w słowniku

import pickle

slownik = {"name": "Radek", "age": 78}
print(type(slownik))  # <class 'dict'>
print(slownik)  # {'name': 'Radek', 'age': 78}

with open("dickt1.pkl", "wb") as f:
    pickle.dump(slownik, f)

with open("dickt1.pkl", "rb") as f:
    data = pickle.load(f)

print(data)  # {'name': 'Radek', 'age': 78}

