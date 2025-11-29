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


print(f"{KalkulatorTemperatur.fahrenheit_to_celcius(100):.2f}")  # 37.78
print(f"{KalkulatorTemperatur.fahrenheit_to_celcius(2):.2f}")  # -16.67

print(f"{KalkulatorTemperatur.celcius_to_farenheit(37.78):.2f}")  # 100.00

assert 100.0 == KalkulatorTemperatur.celcius_to_farenheit(37.78)
# assert 100.0 == KalkulatorTemperatur.celcius_to_farenheit(37.7777777778)
# Traceback (most recent call last):
#   File "/Users/radoslawjaniak/PycharmProjects/BootCamp-11-10-2025A/day_7_29_11_2025/kl12a.py", line 44, in <module>
#     assert 100.0 == KalkulatorTemperatur.celcius_to_farenheit(37.7777777778)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# AssertionError
