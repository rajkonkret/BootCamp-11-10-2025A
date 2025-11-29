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
        print("Tu", self.gatunek, 'Lecę z szybkością', self.szybkosc)

    def wydaj_odglos(self):
        pass


class Kura(Ptak):
    def __init__(self, gatunek):
        super().__init__(gatunek, 0)

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam")

    def wydaj_odglos(self):
        print("Ko ko ko ko ko")


or1 = Ptak("Orzeł", 45)
or1.latam()  # tu Orzeł Lecę z szybkością 45

kur1 = Ptak("Kura", 0)
kur1.latam()  # tu Kura Lecę z szybkością 0

kur2 = Kura("Kura złocista")
kur2.latam()  # Tu Kura złocista Ja nie latam
