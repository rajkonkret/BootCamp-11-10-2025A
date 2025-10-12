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


