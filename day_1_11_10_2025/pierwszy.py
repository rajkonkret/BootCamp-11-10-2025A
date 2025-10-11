# PEP 8 – Style Guide for Python Code
# https://peps.python.org/pep-0008/
# snake_case - konwencja nazewnicza
# ctrl alt l
import sys

print()  # wypisz/wydrukuj

print("Nazywam się Radek")  # Nazywam się Radek
print("Nazywam się Radek")  # Nazywam się Radek
print("Nazywam się Radek")  # Nazywam się Radek
print("Nazywam się Radek")  # Nazywam się Radek
print("Nazywam się Radek")  # Nazywam się Radek
print("Nazywam się Radek")  # Nazywam się Radek
# ctrl d - powielanie linii

print('Nazywam się Radek')  # Nazywam się Radek
# Process finished with exit code 0 - program zakończył się poprawnie

# ctrl / - komentowanie linijki
# print('Nazywam się Radek")
#   File "/Users/radoslawjaniak/PycharmProjects/BootCamp-11-10-2025A/day_1_11_10_2025/pierwszy.py", line 19
#     print('Nazywam się Radek")
#           ^
# SyntaxError: unterminated string literal (detected at line 19)
#
# Process finished with exit code 1 - bład wykonania programu
print("Dalsza część programu")

# type() - sprawdzenie typu danych
print(type("Radek"))  # <class 'str'>, string,, typ tekstowy

print("39" + "14")  # 3914, konkatenacja, łaczenie stringów

print(39)  # 39
print(type(39))  # <class 'int'>, liczby całkowite, integer

print(39 + 14)  # 53

# print("39" + 14)  # TypeError: can only concatenate str (not "int") to str

# rzutowanie
print(int("39") + 14)  # 53 int() - rzutowanie na int
print("39" + str(14))  # 3914 - rzutowanie na str

print(5 * "4")  # 44444
print(35 * 168)  # 5880
print(35 * "168")
# 168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168

# zakres int
print(sys.int_info)
# sys.int_info(bits_per_digit=30,
#              sizeof_digit=4,
#              default_max_str_digits=4300,
#              str_digits_check_threshold=640)

# zmienna - pudełko na dane
# snake_case
# wg PEP8 nazwa zmiennej powinna podpowiadać co zawiera

# typowanie dynamiczne
# mozna do zmiennej dowolny typ danych wrzucić w każdej chwili
name = "Radek"  # wpisanie wartości do zmiennej
print(type(name))  # <class 'str'>
print(name)  # Radek - wypisanie zawartości zmiennej

name = 90
print(type(name))  # <class 'int'>
print(name)  # 90

name_info = "Radek"  #
# print(19 + name_info)  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# podpowiedzi typu
name_info: str = "Maciek"
print(name_info)  # Maciek
name_info = 90
print(name_info)  # 90

# pip install mypy - instalacja programu - sprawdza zgodność typów  w programie pythonowym
# cd day_1_11_10_2025  wejście do katalogu
# (.venv) radoslawjaniak@mac day_1_11_10_2025 % mypy pierwszy.py
# pierwszy.py:67: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
# pierwszy.py:75: error: Name "name_info" already defined on line 71  [no-redef]
# pierwszy.py:77: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
# Found 3 errors in 1 file (checked 1 source file)
# (.venv) radoslawjaniak@mac day_1_11_10_2025 %

age = 48
print(age)  # 48
print(type(age))  # <class 'int'>
