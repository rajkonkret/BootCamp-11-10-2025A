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

# pop() - usunięcie pierwszego eleemntu
print(zbior.pop())  # 33
print(zbior)  # {66, 777, 11, 44, 18, 22, 55}

print(zbior.pop())  # 66
zbior.pop()
zbior.pop()
print(zbior)  # {44, 18, 22, 55}

# użycie sorted() na zbiorze
# zwróci nam listę posortowanych elementów
print(sorted(zbior))  # [18, 22, 44, 55]

# usunięcie elementu ze zbioru po wskazanym elemencie
zbior.remove(55)
zbior.remove(18)
print(f"Zbiór po usunięciu: {zbior=}")  # Zbiór po usunięciu: zbior={44, 22}
print(f"Zbiór po usunięciu: {zbior}")  # Zbiór po usunięciu: {44, 22}

# tworzenie zbioru z konkretnymi wartościami
zbior2 = {667, 11, 44, 18, 52, 22, 667, 62, 999}
print(zbior2)  # {999, 11, 44, 18, 52, 22, 667, 62}
print(type(zbior2))  # <class 'set'>

zbior3 = {667, 11, 44, 18, 667, 62, 999}
print(zbior3)  # {18, 999, 11, 44, 667, 62}

# suma zbiorów
# wszystkie elementy pierwszego i drugiego zbioru
# nie ma duplikatów!!!
# tworzy nowy zbiór
print(zbior | zbior3)  # {999, 11, 44, 18, 22, 667, 62}
print(zbior.union(zbior3))  # {999, 11, 44, 18, 22, 667, 62}

# zbiory bazowe nie zmieniły się
print(zbior)  # {44, 22}
print(zbior3)  # {18, 999, 11, 44, 667, 62}

print(zbior2 | zbior3)  # {999, 11, 44, 18, 52, 22, 667, 62}
print(zbior2.union(zbior3))  # {999, 11, 44, 18, 52, 22, 667, 62}

# zbiory bazowe nie zmieniły się
print(zbior2)  # {999, 11, 44, 18, 52, 22, 667, 62}
print(zbior3)  # {18, 999, 11, 44, 667, 62}

zbior4 = {8, 9, 10}
print(zbior.union(zbior3, zbior4))
# {999, 8, 9, 10, 11, 44, 18, 22, 667, 62}
print(zbior | zbior3 | zbior4)
# {999, 8, 9, 10, 11, 44, 18, 22, 667, 62}

# część wspólna - zwraca nowy zbiór
print(zbior2 & zbior3)  # {999, 11, 44, 18, 667, 62}
print(zbior2.intersection(zbior3))  # {999, 11, 44, 18, 667, 62}
