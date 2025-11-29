# utility class
# metody statyczne

class Matematyka:

    @staticmethod
    def dodaj(a, b):
        return a + b

    @staticmethod
    def odejmij(a, b):
        return a - b


# mat = Matematyka()
wynik = Matematyka.dodaj(5, 6)
print(wynik)  # 11
wynik = Matematyka.odejmij(65, 34)
print(wynik)  # 31


# klasa z metodami statycznymmi
# celcjusz -> farnheit
# farenheit -> celcjusz
# (°F - 32) x 5/9 =°C
# (°C x 9/5) + 32 =°F

class KalkulatorTemperatur:

    @staticmethod
    def celcius_to_farenheit(celcius):
        return celcius * 9 / 5 + 32

    @staticmethod
    def fahrenheit_to_celcius(farenheit):
        return (farenheit - 32) * 5 / 9
