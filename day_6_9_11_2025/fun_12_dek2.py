from functools import wraps

from colorama import Fore, Style, init

init(autoreset=True)


# napisać dekorator, który zmieni wynik dziłania funkcji na duże litery
def upper_case_decorator(fun):
    def wrapper():
        result = fun()  # uruchomienie funkcji
        return result.upper()  # zmian ana duże litery

    return wrapper


# pogrubienie liter
def bold_decorator(fun):
    def wrapper():
        result = fun()  # uruchomienie funkcji
        return "\033[1m" + result + "\033[0m"

    return wrapper


def color_decorator(fun):
    @wraps(fun)  # pozwala zachować metadane
    def wrapper(*args, **kwargs):  # przejmie wszystkie parametry
        print(fun.__name__)
        result = fun(*args, **kwargs)
        return Fore.RED + result

    return wrapper


@upper_case_decorator
def greeting():
    return "Hello World!"


@bold_decorator
@upper_case_decorator
def greeting2():
    return "Hello World!"


@color_decorator
def greeting3():
    return "Hello World!"


@color_decorator
def greeting4(string):
    return f"Hello World! {string}"


print(greeting())  # HELLO WORLD!
# print()
print(greeting2())
print(greeting3())
print(greeting4("Radek"))
print(greeting4.__name__)  # wrapper


# po uzyciu @wraps() -> greeting4


def dekor_z_arg(param):
    def dekor(func):
        def wew():
            print("Dekorator przekazał:", param)
            return func()

        return wew

    return dekor


@dekor_z_arg("HeLO")
def funcja_argument():
    print("Oryginalna funkcja")


funcja_argument()
# Dekorator przekazał: HeLO
# Oryginalna funkcja
