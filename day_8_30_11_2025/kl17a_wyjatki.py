# wyjątki
# błedy podczas wykonywania programu
# mozemy tworzyć własne wyjatki
# dziedziczymy po klasie Exception

# print(2 / 0)  # ZeroDivisionError: division by zero
# raise ZeroDivisionError("Nie dziel przez zero")  # ZeroDivisionError: Nie dziel przez zero

class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)


# raise MyException("Wyjątek od Radka")
# Traceback (most recent call last):
#   File "/Users/radoslawjaniak/PycharmProjects/BootCamp-11-10-2025A/day_8_30_11_2025/kl17a_wyjatki.py", line 13, in <module>
#     raise MyException("Wyjątek od Radka")
# MyException: Wyjątek od Radka

try:
    x = int(input("Podaj liczbę cąlkowitą dodatnią:"))
    if x < 0:
        print("Liczba ma być większa od zera")
        raise MyException("Liczba musi byc dodatnia")
except MyException as e:
    print("Wystąpił wyjątek MyException:", e)
except ValueError:
    print("Błąd wartości")
except Exception as e:  # pozostałę błędy
    print("Błąd:", e)
else:  # gdy nie ma błedu
    print("Wprowadziłęś poprawną odpowiedź")
finally:  # wypisze zawsze
    print('Wprowadź kolejne dane')

# Podaj liczbę cąlkowitą dodatnią:-9
# Liczba ma być większa od zera
# Wystąpił wyjątek MyException: Liczba musi byc dodatnia

# Podaj liczbę cąlkowitą dodatnią:10
# Wprowadziłęś poprawną odpowiedź
# Wprowadź kolejne dane
