class Car:
    """
    Klasa opisująca samochód w pythonie
    """

    def __init__(self, model, year):
        self.model = model
        self.year = year
        # hermetyzacja
        # pole prywatne
        self.__predkosc = 0

    def gaz(self):
        self.__predkosc += 10

    def licznik(self):
        print(f"Prędkość wynosi {self.__predkosc} km/h.")

    def __zmien_bieg(self):
        print("Zmiana biegu")

    def hamuj(self):
        if self.__predkosc > 0:
            self.__predkosc -= 10
            self.__zmien_bieg()
        else:
            self.__predkosc = 0
            print("Zatrzymałeś się")


car = Car("Ferrari", 2025)
car.gaz()
car.gaz()
car.gaz()
car.gaz()
car.gaz()
# AttributeError: 'Car' object has no attribute '__predkosc'. Did you mean: '_Car__predkosc'?
# pole oznaczone jako prywatne
# print(car.__predkosc)  # 50
car.licznik()  # Prędkość wynosi 50 km/h.
car.__predkosc = 0  # pole publiczne o tej samej nazwie
car.__predkosc = 5  # km? mile?
car.licznik()  # Prędkość wynosi 50 km/h.
# car.__zmiana_biegu() # AttributeError: 'Car' object has no attribute '__zmiana_biegu'

car.hamuj()
car.hamuj()
car.hamuj()
car.hamuj()
car.hamuj()
car.licznik()
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Prędkość wynosi 0 km/h.
car.hamuj()
car.licznik()
# Prędkość wynosi -10 km/h.
# -------
# Prędkość wynosi 0 km/h.
# Zatrzymałeś się
# Prędkość wynosi 0 km/h.
