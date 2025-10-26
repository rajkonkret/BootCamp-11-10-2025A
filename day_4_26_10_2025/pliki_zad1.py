# praca z plikami

# ========= ===============================================================
#     Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     ========= ===============================================================
# filehandler - narzędzie do działania z konkretnym plikiem
fh = open("test_fh.txt", "w", encoding="utf-8")
fh.write("Radek\n")  # zapis danych do pliku
fh.close()  # zamknięcie dostępu do pliku

# contezt manager - pozwal na bezpieczniejszą pracę z plikami
# with - context manager w pythonie
# zadba o zamknięcie pliku nawet gdy podczas operacji dyskowej wystąpi błąd
with open("test.log", "w", encoding="utf-8") as file:
    file.write("Radek\n")
    file.write("Kolejna linia\n")
    file.write("Jescze jedna\n")

# plik w katalogu nadrzędnym (piętro wyżej)
with open("../test.log", "w", encoding="utf-8") as file:
    file.write("Radek\n")
    file.write("Kolejna linia\n")
    file.write("Katalog nadrzędny\n")

# w - plik zostanie skasowany jeśli istnieje
with open("../test.log", "w", encoding="utf-8") as file:
    file.write("Nowe dane\n")
    file.write("Kolejna linia\n")
    file.write("Katalog nadrzędny\n")

# x  - gdy plik juz istnieje dostaniemy bład: FileExists
# FileExistsError: [Errno 17] File exists: '../test.log'
# with open("../test.log", "x", encoding="utf-8" as file:
#     file.write("Nowe dane\n")
#     file.write("Kolejna linia\n")
#     file.write("Katalog nadrzędny\n")
# gdy nie istnieje, zostanie utwworzony
# with open("../test2.log", "x", encoding="utf-8") as file:
#     file.write("Nowe dane\n")
#     file.write("Kolejna linia\n")
#     file.write("Katalog nadrzędny\n")
#     file.write("Dopisane1\n")

# a - dopisuje na końcu istniejącego pliku
with open("../test.log", "a", encoding="utf-8") as file:
    file.write("Nowe dane\n")
    file.write("Kolejna linia\n")
    file.write("Dopisane2\n")

with open("test.log", "a", encoding="utf-8") as file:
    file.write("Nowe dane\n")
    file.write("Kolejna linia\n")
    file.write("Dopisane2\n")
    file.write("Dośąźdane\n")

# r - odczytanie pliku
with open("test.log", "r", encoding="utf-8") as f:
    lines = f.read()

print(lines)
# Radek
# Kolejna linia
# Jescze jedna
# Nowe dane
# Kolejna linia
# Dopisane2
# encoding="utf-8" - wymuszenie kodowania utf-8

with open("linie.txt", "w") as f:
    f.write("Pierwsza linia\n")
    f.write("Druga linia\n")
    f.write("Trzecia linia\n")

with open("linie.txt", "r") as fh:
    tekst = fh.read()

print(tekst)
# Pierwsza linia
# Druga linia
# Trzecia linia
print(repr(tekst))  # 'Pierwsza linia\nDruga linia\nTrzecia linia\n'

print(50 * "-")
with open('linie.txt', "r") as fh:
    linie = fh.readlines()

print(linie)  # ['Pierwsza linia\n', 'Druga linia\n', 'Trzecia linia\n']

print(50 * "-")
with open("linie.txt", "r") as f:
    jedna_linia = f.readline()
print(jedna_linia)  # Pierwsza linia

print(50 * "-")
with open('linie.txt', "r") as file:
    for linia in file:
        print(linia.strip())
# --------------------------------------------------
# Pierwsza linia
# Druga linia
# Trzecia linia

print(50 * "-")
# plik musi istniec
with open('linie.txt', "r+") as f:
    lines = f.readlines()
    f.seek(0)  # wracamy na początek pliku
    f.write("Nowa wiadomoc \n")
    f.writelines(lines[1:])  # pozostałe linia
    f.truncate()  # jeśli nowa linia ma mniej danych niż dotychczasowa, usunie zbędne dane
print(lines)

print(50 * "-")
# w+ tworzy nowy plik i pozwala od razu odczytac z niego dane
with open("plik.txt", "w+") as f:
    f.write("Nowa linia\n")
    f.seek(0)  # wraca na początek pliku
    print(f.read())
# Nowa linia
