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
