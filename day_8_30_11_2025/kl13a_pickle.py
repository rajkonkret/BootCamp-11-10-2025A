# pickle - serializacja i deserializacja obiektów
import pickle
import ast

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

# serializacja
with open('lista.pickle', "wb") as f:
    pickle.dump(lista, f)  # zapis listy do pliku w postaci bajtowej

# deserializacja
with open("lista.pickle", 'rb') as fh:
    p = pickle.load(fh)

print(p)  # [1, 2, 3, 4, 5]
print(type(p))  # <class 'list'>
print(p[0])
print(50 * "-")

# zamiana listy na bajty
lista_ser = pickle.dumps(lista)
print(lista_ser)
# b'\x80\x04\x95\x0f\x00\x00\x00\x00\x00\x00\x00]\x94(K\x01K\x02K\x03K\x04K\x05e.'

# zamiana bajtów na listę
wynik = pickle.loads(lista_ser)
print("Wynik deserializacji:", wynik)  # Wynik deserializacji: [1, 2, 3, 4, 5]
print(type((wynik)))  # <class 'list'>

with open('lista.txt', "r") as file:
    lines = file.read()

print(lines)
print(type(lines))
# [1, 2, 3, 4, 5]
# <class 'str'>

lista_eval = eval(lines)
print(type(lista_eval))  # <class 'list'>
print(lista_eval)  # [1, 2, 3, 4, 5]
print(lista_eval[0])  # 1

# istnieje mozliwosc przekazania i wykonania złosliwego kodu
user_input = "print('hacked')"
eval(user_input)  # hacked, wykona komendę przekazaną tekstem

# bezpieczniejsze podejscie
lista = ast.literal_eval(lines)
print(lista)  # [1, 2, 3, 4, 5]
print(type(lista))  # <class 'list'>
