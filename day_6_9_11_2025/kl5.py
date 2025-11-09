# dziedziczenie
class Pojazd:
    def __init__(self, kolor):
        self.kolor = kolor

    def info(self):
        print(f"Kolor: {self.kolor}")


poj = Pojazd("Czerwony")
poj.info()


class Samochod(Pojazd):
    """
    Klasa Samochód, dziedziczy po klasie Pojazd
    """

    def __init__(self, kolor, marka="Fiat"):
        # obowiązkowo musimy wywołac konstruktor z klasy wyzszej
        # super() - klasa nadrzędna(ta po której dziedziczymy)
        super().__init__(kolor)
        self.marka = marka

    def info(self):
        super().info()  # możemy wywołac metodę z klasy super()
        print(f"Marka: {self.marka}")


sam = Samochod("Zielony")
sam.info()
# Kolor: Zielony
# Marka: Fiat

sam2 = Samochod("biały", "Mercedes")
sam2.info()
# Kolor: biały
# Marka: Mercedes
