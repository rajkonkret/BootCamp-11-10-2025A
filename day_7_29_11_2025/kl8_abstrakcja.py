# klasa abstrakcyjna
# klasa z której nie możemy zrobic obiektu
# posiada metode abstrakcyjną
# metoda abstrakcyjna - @abstractmethod

class Ptak:
    """
    Klasa opisująca ptaka w Pythonie
    """

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("tu", self.gatunek, 'Lecę z szybkością', self.szybkosc)
