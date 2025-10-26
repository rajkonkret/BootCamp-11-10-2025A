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
    file.write("Dośdane\n")

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

