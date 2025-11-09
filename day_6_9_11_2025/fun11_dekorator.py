# dekorator - funkcja opakowująca inną funkcję
# przyjmuje funkcje jako argument
# wykorzystuje zasady funkcji wewnętrznej
def dekor(fun):
    def wew():
        print("Dekoruj")
        return fun()  # zwracamy wynik dziłania funkcji

    return wew


@dekor
def hej():
    print("Hej!!")


hej()
# po uzyciu dekor
# Dekoruj
# Hej!!
