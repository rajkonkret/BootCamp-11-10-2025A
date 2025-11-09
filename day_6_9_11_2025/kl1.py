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
    imie = ""
    wiek = None
    plec = "k"

    # self - obiekt klasy
    def powitanie(self):
        print(f"Nazywam sie: {self.imie}")
        # print(f"Nazywam sie: {cz1.imie}")
        # print(f"Nazywam sie: {cz2.imie}")

    # wypisz_wiek()
    def wypisz_wiek(self):
        print(f"Mam {self.wiek} lat.")


print(Human.__doc__)  # Klasa Human opisująca człowieka w pythonie
# print(print.__doc__)
# cd day_6_9_11_2025/ - wejscie do katalogu
# pydoc -b - uruchomienie serwera  zdokumentacją
# python -m pydoc -b
# help("kl1")
# print(pydoc.render_doc("kl1"))
# pydoc -w kl1 - dokumentacja w postaci pliku html

cz1 = Human()
print(cz1)
# <__main__.Human object at 0x1053fd550>
print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)
#
# None
# k

cz1.imie = "Radek"
cz1.wiek = 90
cz1.plec = "m"
print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)
# Radek
# 90
# m

cz2 = Human()
cz2.imie = "Anna"
cz2.wiek = 40
# cz2.plec = "k"
print(cz2.imie)
print(cz2.wiek)
print(cz2.plec)
# Anna
# 40
# k

cz1.powitanie()
cz2.powitanie()
# Nazywam sie: Radek
# Nazywam sie: Anna

cz1.wypisz_wiek()
cz2.wypisz_wiek()
# Mam 90 lat.
# Mam 40 lat.
