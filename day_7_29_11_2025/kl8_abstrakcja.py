# klasa abstrakcyjna
# klasa z której nie możemy zrobic obiektu
# posiada metode abstrakcyjną
# metoda abstrakcyjna - @abstractmethod
from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    Klasa opisująca ptaka w Pythonie
    """

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, 'Lecę z szybkością', self.szybkosc)

    @abstractmethod # metoda abstrakcyjna
    def wydaj_odglos(self):
        pass


class Kura(Ptak):
    def __init__(self, gatunek):
        super().__init__(gatunek, 0)

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam")

    def wydaj_odglos(self):
        print("Ko ko ko ko ko")


class Orzel(Ptak):
    """
    Klasa Orzel dziedziczy po klasie Ptak
    """

    def wydaj_odglos(self):
        print("kier kir kir kier")

# TypeError: Can't instantiate abstract class Sowa without an implementation
# for abstract method 'wydaj_odglos'
class Sowa(Ptak):
    """
    Kalsa Sowa
    """


# TypeError: Can't instantiate abstract class Ptak
# without an implementation for abstract method 'wydaj_odglos'
# or1 = Ptak("Orzeł", 45)
# or1.latam()  # tu Orzeł Lecę z szybkością 45
#
# kur1 = Ptak("Kura", 0)
# kur1.latam()  # tu Kura Lecę z szybkością 0

kur2 = Kura("Kura złocista")
kur2.latam()  # Tu Kura złocista Ja nie latam

or2 = Orzel('Bielik', 50)
or2.latam()  # Tu Bielik Lecę z szybkością 50

# TypeError: Can't instantiate abstract class Sowa
# without an implementation for abstract method 'wydaj_odglos'
# sowa1 = Sowa("Sowa", 25)