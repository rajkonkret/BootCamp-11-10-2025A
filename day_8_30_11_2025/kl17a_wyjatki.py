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

