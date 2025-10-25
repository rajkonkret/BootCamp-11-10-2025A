# wyjatek - błąd podczas wykonywania programu

# print(5 / 0)
# Traceback (most recent call last):
#   File "/Users/radoslawjaniak/PycharmProjects/BootCamp-11-10-2025A/day_3_25_10_2025/wyjatki.py", line 3, in <module>
#     print(5 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero


try:
    # print(5 / 0)
    # print("a" / 2)
    # print(int("A"))
    # raise KeyError("Bład klucza")  # rzucenie błedu jawnie
    wynik = 90 / 3
except ZeroDivisionError:
    print("Nie dziel przez zero")
except TypeError:
    print("Bład typu")
except ValueError:
    print("Błąd wartości")
except Exception as e:
    print("Błąd:", e)
else:  # tylko gdy nie ma błedu
    print("Wynik:", wynik)
finally:  # wykona się zawsze
    print("Kolejna linia")

print("Dalsza czzęść programu")
# Nie dziel przez zero
# Dalsza czzęść programu
# Bład typu
# Dalsza czzęść programu
# Błąd wartości
# Dalsza czzęść programu
# Błąd: 'Bład klucza'
# Dalsza czzęść programu
# Wynik: 30.0
# Dalsza czzęść programu
# Wynik: 30.0
# Kolejna linia
# Dalsza czzęść programu
