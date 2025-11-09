# zasięg zmiennych

a = 10
b = 10


def dodaj():
    a = 6  # zmienne globalne
    b = 8  # nie zmienia wartości zmiennej globalnej
    print(a + b)


def dodaj2():
    print(a + b)  # użyje wartości globalnej


def dodaj3():
    global a  # użyj zmiennej globalnej
    a = 5  # zmienna globalna
    b = 9  # zmienna lokalna
    print(a + b)


print(f"Zmienne a,b z góry (globalne): {a}, {b}")  # Zmienne a,b z góry (globalne): 10, 10
dodaj()  # 14
print(f"Zmienne a,b z góry (globalne): {a}, {b}")  # Zmienne a,b z góry (globalne): 10, 10
dodaj2()  # 20
print(f"Zmienne a,b z góry (globalne): {a}, {b}")  # Zmienne a,b z góry (globalne): 10, 10
dodaj3()  # 14
print(f"Zmienne a,b z góry (globalne): {a}, {b}")  # Zmienne a,b z góry (globalne): 5, 10
dodaj2()  # 15
