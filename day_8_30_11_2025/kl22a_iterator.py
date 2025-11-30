# iterator - pozwala na dostęp sekwencyjny
# zapamiętuje, który eleemnt dostarczył
# oszczędnośc pamięci

# # 1. **Zarządzanie Pamięcią**: Iteratory są efektywne pod względem pamięci,
# # ponieważ nie wymagają wczytywania całego zbioru danych do pamięci na raz.
# # Są one szczególnie użyteczne przy przetwarzaniu dużych zbiorów danych.
# #
# # 2. **Uniwersalność**: Można je stosować do różnych typów struktur danych,
# # ułatwiając pisanie generycznego, wielokrotnego użytku kodu.
# #
# # 3. **Leniwe Wykonanie**: Iteratory realizują leniwe wykonanie,
# # co oznacza, że generują elementy na żądanie, co może być korzystne dla wydajności.

lista = [1, 2, 3, 4, 5]
print(lista)  # [1, 2, 3, 4, 5]
for i in lista:
    print(i)
# 1
# 2
# 3
# 4
# 5

# print(next(lista))  # TypeError: 'list' object is not an iterator

iterator = iter(lista)  # tworzymy iterator z listy
print(iterator)  # <list_iterator object at 0x102c14880>
print(type(iterator))  # <class 'list_iterator'>

# for i in iterator:
#     print(i)
# 1
# 2
# 3
# 4
# 5
print(35 * "-")
print(next(iterator))  # StopIteration - iterator nie ma juz elementów do odczytanie
# 1
print("Zrób cos")
print("Dalej")
print("Uczę się pythona")
for x in range(5):
    print(x, sep="|", end="")
# Zrób cos
# Dalej
# Uczę się pythona
# 01234
print()
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


# print(next(iterator))  # StopIteration

class Count:
    """
    Klasa będąca iteratorem
    """

    def __init__(self, low, high):
        """
        Metodda inicjalizująca (konstruktor)
        :param low:
        :param high:
        """
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1
