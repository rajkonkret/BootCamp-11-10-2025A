# pickle - serializacja i deserializacja obiektów

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
# ['[', '1', ',', ' ', '2', ',', ' ', '3', ',', ' ', '4', ',', ' ', '5', ']']
