# dziedziczenie diamentowe
from pprint import pprint


class A:
    def method(self):
        print("Metoda z klasy A")


class B(A):
    def method(self):
        print("Metoda z klasy B")


class C(A):
    def method(self):
        print("Metoda z klasy C")


class D(B, C):
    """
    Klasa D dziedziczy po klasie B i C a one dziedziczą po klasie A
    """


d = D()
d.method()  # Metoda z klasy B
pprint(D.__mro__)


# (<class '__main__.D'>,
#  <class '__main__.B'>,
#  <class '__main__.C'>,
#  <class '__main__.A'>,
#  <class 'object'>)

# class E(A, D):
#     pass
#
# print(E.__mro__)
# TypeError: Cannot create a consistent method resolution order (MRO) for bases A, D

class F(D, A):
    pass


pprint(F.__mro__)
# (<class '__main__.F'>,
#  <class '__main__.D'>,
#  <class '__main__.B'>,
#  <class '__main__.C'>,
#  <class '__main__.A'>,
#  <class 'object'>)
