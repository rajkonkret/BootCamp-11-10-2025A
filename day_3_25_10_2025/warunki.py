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
