dictionary = {'imie': "Radek", 'nazwisko': "Kowalski"}
print(type(dictionary))
print(dictionary)  # {'imie': 'Radek', 'nazwisko': 'Kowalski'}

# wyswietli tylko klucze
for i in dictionary:
    print(i)
# imie
# nazwisko

for i in dictionary.keys():
    print(i)
# imie
# nazwisko

# wypisanie wartości
for v in dictionary.values():
    print(v)
# Radek
# Kowalski

# wypisanie par
for i in dictionary.items():
    print(i)
# ('imie', 'Radek')
# ('nazwisko', 'Kowalski')

for key, value in dictionary.items():
    print(key, value, sep="<<==>>")
# imie<<==>>Radek
# nazwisko<<==>>Kowalski

for key, value in dictionary.items():
    print(key, value, sep=" : ")
# imie : Radek
# nazwisko : Kowalski
