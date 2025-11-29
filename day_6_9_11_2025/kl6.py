# stworzyc klase Pracownik
# imie, nazwisko, pensja
# przedstaw_sie(), oblicz_pensje()
# zrobic kalse Manager dziedziczącą po klasie Pracownik
# zastonowić co może dziedziczyć bez zmiany, co musi nadpisac w klasie Manager
# dodac dokumentację

# stworzyc jedego pracownika i jedego managera
# użyc metod z klas
class Pracownik:
    def __init__(self, imie, nazwisko, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja

    def przedstaw_sie(self):
        print(f"Cześć, jestem {self.imie} {self.nazwisko}")

    def oblicz_pensja(self):
        return self.pensja


class Manager(Pracownik):
    """
    Klasa dziedziczy po kalsie Pracownik
    """

    def __init__(self, imie, nazwisko, pensja, premia):
        super().__init__(imie, nazwisko, pensja)
        self.premia = premia

    def oblicz_pensja(self):
        return self.pensja + self.premia


pracownik = Pracownik("Jan", "Kowalski", 5000)
pracownik.przedstaw_sie()
wyn_prac = pracownik.oblicz_pensja()
print(f"Wynagrodzenie dla pracownika {pracownik.imie} {pracownik.nazwisko}: {wyn_prac}")
# Cześć, jestem Jan Kowalski
# Wynagrodzenie dla pracownika Jan Kowalski: 5000

manager = Manager("Anna", "Nowak", 10000, 3000)
manager.przedstaw_sie()
wyn_menago = manager.oblicz_pensja()
print(f"Wynagrodzenie dla managera {manager.imie} {manager.nazwisko}: {wyn_menago}")
# Cześć, jestem Anna Nowak
# Wynagrodzenie dla managera Anna Nowak: 13000
