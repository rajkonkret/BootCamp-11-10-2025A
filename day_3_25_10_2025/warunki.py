# instrukcje warunkowe
# instrukcje sterowania przepływem programu
# if - sterowanie warunkiem
# if warunek:
#   komenda(blok) - wykonan gdy warunek spełniony

odp = True
print(bool(odp))
# odp = False
# debuger - pozwala wykonac prokram krok po kroku
# daje możliwość weryfikacji wartośći zmiennych i parametrów
# pułąpka - program zatrzyma się tutaj w trybie debug
if odp:
    # blok wykonywany gdy warunek spełniony
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")

print("Dalsza część programu")
# True
# Brawo
# Brawo
# Brawo
# Brawo
# Brawo
# Brawo
# Dalsza część programu

odp = "Radek"
print(bool(odp))  # True

if odp:
    print("OK")  # OK

odp = "Tomek"
if odp == "Radek":
    print("Radek")
else:  # w przeciwnym wypadku, default
    print("Inny pacjent")
# Inny pacjent


# podatek = 0.9
# zarobki = int(input("Podaj dochód"))
# # jeden spełniony warunek - wychodzi z drzewka
# # koljnośc ma znaczenie
# if zarobki < 10_000:
#     podatek = 0.0
# elif zarobki < 40_000:
#     podatek = 0.2
# elif zarobki < 100_000:
#     podatek = 0.4
# else:
#     podatek = 0.9
#
# print(f"Płacisz {zarobki * podatek} pln podatku.")
# # 0.2 dla przedziału 10_000 do 39_999

suma_zam = 250
if suma_zam > 150:
    rabacik = 25
else:
    rabacik = 0

print(f"Rabat wynosi: {rabacik}")  # Rabat wynosi: 25

# operator warunkowy
rabat = 25 if suma_zam > 150 else 0
print(f"Rabat wynosi: {rabat}")  # Rabat wynosi: 25

# zasymuluj system zbierania logów
# w zmiennej otrzymamy typ systemu: console, email, inny
# w zależności od wartości zmiennej:
# console -> "Stało się coś strasznego"
# email -> "Sytem email"
# jeżleli będzie to system: email, to należy do listy błedów dodac opis błedu
# druga zmienna: przechowuje typ błędu
# error, medium, inny
# "Krytyczny"

alert_system = "email"
error_level = "medium"
lista_b = []

if alert_system == "console":
    print("Stało się coś strasznego")
elif alert_system == "email":
    print("System email")
    if error_level == "error":
        lista_b.append("Krytyczny")
    elif error_level == "medium":
        lista_b.append("Ostrzeżenie")
    else:
        lista_b.append("Inny")
else:
    print("Inny system")

print(lista_b)
# System email
# ['Ostrzeżenie']
