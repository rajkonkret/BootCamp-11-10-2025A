# pickle - serializacja i deserializacja obiektów
import pickle

lista = [1, 2, 3, 4, 5]

with open('lista.txt', "w") as f:
    f.write(str(lista))

with open('lista.txt', "r") as file:
    lines = file.read()

print(lines)
print(type(lines))  # <class 'str'>
print(lines[0])  # "["
l = []
l.extend(lines)
print(l)
# ['[', '1', ',', ' ', '2', ',', ' ', '3', ',', ' ', '4', ',', '

with open('lista.pickle', "wb") as f:
    pickle.dump(lista, f)  # zapis listy do pliku w postaci bajtowej

with open("lista.pickle", 'rb') as fh:
    p = pickle.load(fh)

print(p)  # [1, 2, 3, 4, 5]
print(type(p))  # <class 'list'>
print(p[0])
print(50 * "-")
