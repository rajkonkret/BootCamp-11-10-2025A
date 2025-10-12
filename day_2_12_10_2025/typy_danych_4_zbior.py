# zbior (set) - przechowują unikalne wartości (brak duplikatów)
# nie posiada indeksu
# nie zachowuje kolejności przy dodawaniu elementów

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
print(type(lista))  # <class 'list'>

zbior = set(lista)
# usunięte duplikaty
# zmieniona kolejnosc
print(zbior)  # {33, 66, 777, 11, 44, 22, 55}

# ponowna zamiana na listę i usunięcie wcześniej zduplikowanej wartości
lista2 = list(zbior)
print(lista2)  # [33, 66, 777, 11, 44, 22, 55]
lista2.remove(33)
print(lista2)  # [66, 777, 11, 44, 22, 55]

# utworzenie pustego zbioru (set)
# tylko za pomocą metody set()
zb2 = set()
print(zb2)  # set()
print(type(zb2))  # <class 'set'>

# dodawanie elementów do zbioru
zb2.add(2)
zb2.add(3)
zb2.add(5)
zb2.add(5)
zb2.add(3)
print(zb2)  # {2, 3, 5}

print(zbior)  # {33, 66, 777, 11, 44, 22, 55}
zbior.add(33)
zbior.add(33)
zbior.add(18)
zbior.add(18)
zbior.add(22)
print(zbior)  # 33, 66, 777, 11, 44, 18, 22, 55}
# zamienił kolejność
