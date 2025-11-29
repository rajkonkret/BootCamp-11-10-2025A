class Animal:

    def __init__(self, name):
        self.name = name

    def wydaj_odglos(self):
        pass

    def info(self):
        print(f"Imię: {self.name}")


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)  # musimy użyć metody z klasy wyższej
        self.color = color

    def wydaj_odglos(self):
        print("miau miau")

    def info(self):
        super().info()  # mozemy użyc metodyz  klasy wyższej
        print(f"Kolor: {self.color}")


class Tiger(Cat):
    def __init__(self, name, color, liczba_paskow):
        super().__init__(name, color)
        self.liczba_paskow = liczba_paskow

    def wydaj_odglos(self):
        print("arr arr!!!")

    def info(self):
        super().info()
        print(f"Liczba pasków: {self.liczba_paskow}")


