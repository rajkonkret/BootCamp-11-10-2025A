# klasa - szablon, przepis, wzor
# obiekt - zbudowany wg przepiu, instancja klasy
# pola, funkcje (metody)
# klasa musi byc najpierw zadeklarowana
# tworzenie obiektu uruchmia metodę __init__ (konstruktor)
# paradygmaty:
# enkapsulacja, hermetyzacja, polimorfizm, dziedziczenie, abstrakcja
import pydoc


# PascalCase -> UpperCamelCase
# deklaracja klasy
class Human:
    """
    Klasa Human opisująca człowieka w pythonie
    """


print(Human.__doc__)  # Klasa Human opisująca człowieka w pythonie
print(print.__doc__)
# cd day_6_9_11_2025/ - wejscie do katalogu
# pydoc -b - uruchomienie serwera  zdokumentacją
# python -m pydoc -b
help("kl1")
print(pydoc.render_doc("kl1"))
# pydoc -w kl1 - dokumentacja w postaci pliku html
