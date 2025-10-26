import os

print(os.path.abspath("json_zad1.py"))
# /Users/radoslawjaniak/PycharmProjects/BootCamp-11-10-2025A/day_4_26_10_2025/json_zad1.py

current_dir = os.getcwd()
# for root, dirs, files in os.walk("../.."): # cały /Users
# for root, dirs, files in os.walk("../"): # nasz katalog nadrzędny
for root, dirs, files in os.walk(current_dir): # nasz katalog bieżący
    abs_root = os.path.abspath(root)
    # print(abs_root)
    if dirs:
        print("Directories")
        for dir_ in dirs:
            print(dir_)

    if files:
        print("Files")
        for filename in files:
            print(filename)
# Files
# petle_zad3.py
# plik.txt
# pliki_zad1.py
# petle_zad2.py
# nasze_dane_sort.json
# linie.txt
# test.log
# nasze_dane.json
# json_zad1.py
# test_fh.txt
# petle_zad_kalkulator.py
# petle_zad_chtgpt.py
# nasze_dane_b.json
# discount.py
# dir_walking.py
# pliki_zad2.py