# Kolekcje

# lista - kolekcja przechowująca dowolną ilość danych, dowolnego typu na raz
# może w jedej liście przechowywać np.: str, int, bytes...
# lista zachowuje kolejnosc przy dodawaniu elementów, trafia na koniec listy

# tworzenie pustej listy
lista = []
print(lista)  # []
print(type(lista))  # <class 'list'>
print(bool(lista))  # False

pusta_lista = list()
print(pusta_lista)  # []
print(type(pusta_lista))  # <class 'list'>

# deklaracja listy i wypełnienie w miejscu deklaracji
lista_2 = [10, 20, 30]
print(type(lista_2))  # <class 'list'>
print(lista_2)  # [10, 20, 30]

lista_3 = [10.77, 30.66, 67, 15]
print(type(lista_3))  # <class 'list'>
print(lista_3)  # [10.77, 30.66, 67, 15]

# lista mieszana
lista_mieszane = [10, 5.2, "Oko", "Radek"]
print(type(lista_mieszane))  # <class 'list'>
print(lista_mieszane)  # [10, 5.2, 'Oko', 'Radek']

# sprawdzenie ile eleemntów znajduje się w kolekcji
print(len(lista_mieszane))  # długość 4
# [10, 5.2, 'Oko', 'Radek']
#   0   1     2       3    indeksowanie od 0

# dodawanie elementów do listy
lista.append("Radek")  # dodaje na końcu listy
lista.append("Maciek")  # dodaje na końcu listy
lista.append("Tomek")  # dodaje na końcu listy
lista.append("Zenek")  # dodaje na końcu listy
lista.append("Marta")  # dodaje na końcu listy
lista.append("Anna")  # dodaje na końcu listy
print(lista)  # ['Radek', 'Maciek', 'Tomek', 'Zenek', 'Marta', 'Anna']

print(type(lista))  # <class 'list'>
print(len(lista))  # długość 6 elementów

# ['Radek', 'Maciek', 'Tomek', 'Zenek', 'Marta', 'Anna']
#     0         1         2       3         4       5
#     -6        -5        -4      -3       -2       -1

# wypisanie elementów po indeksie
print(lista[1])  # Maciek
print(lista[3])  # Zenek
print(lista[5])  # Anna

# len(lista) - 1 - indeks ostatniego elementu
print(lista[len(lista) - 1])  # Anna, ostatni element
print(lista[-1])  # Anna, ostatni
print(lista[-2])  # Marta
print(lista[-3])  # Zenek
print(lista[-4])  # Tomek
print(lista[-5])  # Maciek
print(lista[-6])  # Radek

# ctrl c
# kólko myszy dla wszystkich wierszy
# wstawiamy #
# stawiamy kursor w dowolnym miejscu
# column selection mode on
# ctrl v
# column selection mode off
# ctrl alt l

# ['Radek', 'Maciek', 'Tomek', 'Zenek', 'Marta', 'Anna']
#     0         1         2       3         4       5
#     -6        -5        -4      -3       -2       -1
# print(lista[10])  # IndexError: list index out of range

# print(lista[-7])  # IndexError: list index out of range
wynik = len(lista) - 1
print(wynik)  # 5
wynik = len(lista) - 8
print(wynik)  # -2

# slicowanie - zwraca listę
print(lista[0:3])  # ['Radek', 'Maciek', 'Tomek'] 012
print(lista[:3])  # ['Radek', 'Maciek', 'Tomek']

print(lista[1:3])  # ['Maciek', 'Tomek']
print(lista[:2])  # ['Radek', 'Maciek']
print(lista[-3:])  # ['Zenek', 'Marta', 'Anna'] włącznie z ostatnim
print(lista[-2:])  # ['Marta', 'Anna']
print(lista[-1:])  # ['Anna'] - lista z jednym elementem
print(lista[-1:][0])  # Anna - element listy, indeks 0 -> Anna, str
print(lista[-1])  # Anna element nie lista
print(lista[-1][0])  # A

print(lista[:])  # ['Radek', 'Maciek', 'Tomek', 'Zenek', 'Marta', 'Anna']

print(lista[2:5])  # indeksy 234, ['Tomek', 'Zenek', 'Marta']
print(lista[2:])  # indeksy 2345, ['Tomek', 'Zenek', 'Marta', 'Anna'] z ostatnim włącznie

# ['Radek', 'Maciek', 'Tomek', 'Zenek', 'Marta', 'Anna']
#     0         1         2       3         4       5
#     -6        -5        -4      -3       -2       -1
print(lista[-3:0])  # [] -> [3:0]
print(lista[0:-3])  # ['Radek', 'Maciek', 'Tomek']

print(lista[2:2])  # []
print(lista[2:3])  # ['Tomek'] indeks2, bez trzeciego
print(lista[4:10])  # ['Marta', 'Anna'] - zwróci elementy do ostatniego włacznie
print(lista[10:20])  # []

# ['Radek', 'Maciek', 'Tomek', 'Zenek', 'Marta', 'Anna']
# rozszerzenie listy, wstawieni elementu we wskazanym indeksie
lista.insert(1, "Karolina")
print(lista)
# ['Radek', 'Karolina', 'Maciek', 'Tomek', 'Zenek', 'Marta', 'Anna']
print(len(lista))  # długośc 7

# usunięcie elementu z listy
# 1. usunięcie po indeksie -> pop()
# 2. usunięcie po elemenecie -> remove()

# po indeksie pop(), zwraca eleemnt usunięty
print(lista.pop(0))  # Radek
print(lista)  # ['Karolina', 'Maciek', 'Tomek', 'Zenek', 'Marta', 'Anna']
ind = lista.index("Zenek")
print("Numer indeksu dla Zenka:", ind)  # Numer indeksu dla Zenka: 3
lista.append("Zenek")
print(lista)
# ['Karolina', 'Maciek', 'Tomek', 'Zenek', 'Marta', 'Anna', 'Zenek']
# zwraca pierwszy napotkany
ind = lista.index("Zenek")
print("Numer indeksu dla Zenka:", ind)  # Numer indeksu dla Zenka: 3
print(lista.pop(ind))  # Zenek
print(lista)  # ['Karolina', 'Maciek', 'Tomek', 'Marta', 'Anna', 'Zenek']

print(lista.pop())  # Zenek, usunie ostatni element
print(lista)  # ['Karolina', 'Maciek', 'Tomek', 'Marta', 'Anna']

# usnięcie po elemencie
lista.append("Maciek")  # dodanie elementu do listy
print(lista)
# remove nie zwraca elementu, który usunie
lista.remove("Maciek")  # usunie pierwsze wystąpienie lementu "Maciek"
print(lista)  # ['Karolina', 'Tomek', 'Marta', 'Anna', 'Maciek']

# lista.remove("Filip")  # ValueError: list.remove(x): x not in list

# sprawdzenie czy element istnieje w liście
print("Marta" in lista)  # True
print("Filip" in lista)  # False

print(lista.remove("Marta"))  # None
# element został usunięty z listy
print(lista)  # ['Karolina', 'Tomek', 'Anna', 'Maciek']

lista.append("Marta")
lista.append("Marta")
lista.append("Marcin")
print(lista)
# ['Karolina', 'Tomek', 'Anna', 'Maciek', 'Marta', 'Marta', 'Marcin']

# odczyta indeks dla pierwszego napotkanego elementu
print(lista.index("Marta"))  # indeks numer 4

a = 1
b = 3
print(f"{a=}, {b=}")  # a=1, b=3
a = b
print(f"{a=}, {b=}")  # a=3, b=3
b = 7
print(f"{a=}, {b=}")  # a=3, b=7

lista_4 = lista  # -> a = b, kopiowianie adresu w pamięci, kopia referencji
print("Lista:", lista)
print("Lista_4:", lista_4)
# Lista: ['Karolina', 'Tomek', 'Anna', 'Maciek', 'Marta', 'Marta', 'Marcin']
# Lista_4: ['Karolina', 'Tomek', 'Anna', 'Maciek', 'Marta', 'Marta', 'Marcin']

lista_copy = lista.copy()  # przekopiowanie wszystkich elementów listy do nowej listy
lista.clear()  # usunięcie eleemntów z listy: lista
print("Lista:", lista)
print("Lista_4:", lista_4)
# Lista: []
# Lista_4: []
print("Lista copy:", lista_copy)
# Lista copy: ['Karolina', 'Tomek', 'Anna', 'Maciek', 'Marta', 'Marta', 'Marcin']

# id() - wskazuje adres w pamięci, gdzie znajduje sie element
print(f"adres: {id(lista)=}")
print(f"adres: {id(lista_4)=}")
print(f"adres: {id(lista_copy)=}")
# adres: id(lista)=4346345024
# adres: id(lista_4)=4346345024
# adres: id(lista_copy)=4348487360

liczby = [45, 999, 34, 22, 13.34, 687]
print(liczby)  # [45, 999, 34, 22, 13.34, 687]
print(type(liczby))  # <class 'list'>

liczby.sort()  # sortowanie listy, zmienia oryginał
print(liczby)  # [13.34, 22, 34, 45, 687, 999]

liczby_a = [45, 999, 34, 22, 13.34, 687, "A"]
print(liczby_a)  # [45, 999, 34, 22, 13.34, 687, 'A']
print(type(liczby_a))  # <class 'list'>

# liczby_a.sort()
# TypeError: '<' not supported between instances of 'str' and 'int'

lista_osoby = ["Radek", "Tomek", "Zenek", "Ania", "Karolina", "Magda"]
lista_osoby.sort()
print(lista_osoby)  # ['Ania', 'Karolina', 'Magda', 'Radek', 'Tomek', 'Zenek']

lista_alfabet = ["a", 'z', "p", 'd']
lista_alfabet.sort()
print(lista_alfabet)  # ['a', 'd', 'p', 'z']

lista_alfabet_pol = ['a', 'z', "ą", "p", "ń", "d"]
lista_alfabet_pol.sort()
print(lista_alfabet_pol)  # ['a', 'd', 'p', 'z', 'ą', 'ń']
print(ord("z"))  # kod znaku: 122, ord() - wypisuje kod ascii znaku
print(ord("ą"))  # kod znaku: 261

# sortowanie i odwrócenie w jednym kroku, zmiana listy
liczby.sort(reverse=True)
print(liczby)  # [999, 687, 45, 34, 22, 13.34]

# # wypisanie w odwrotnej kolejności, bez zmiany oryginalnej listy
# slicowanie - wypisanie fragmentu listy
print(liczby[::-1])  # [13.34, 22, 34, 45, 687, 999] krok -1, [start:stop:krok] - odwrócona kolejność
print(liczby[0:4:2])  # [999, 45]

print(liczby)
print(liczby[-3:0:1])  # []
print(liczby[-3:0:-1])  # [34, 45, 687], działa bo krok -1

# odwrócenie kolekcji, bez sortowania
liczby_3 = [3, 8, 5, 12, 1]
liczby_3.reverse()
print(liczby_3)  # [1, 12, 5, 8, 3]

lista_osoby.reverse()
print(lista_osoby)
# ['Zenek', 'Tomek', 'Radek', 'Magda', 'Karolina', 'Ania']

print(liczby) # [999, 687, 45, 34, 22, 13.34]
