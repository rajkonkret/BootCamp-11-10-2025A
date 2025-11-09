class Human:
    """
    Klasa Human opisująca człowieka w pythonie
    """

    def __init__(self, imie, wiek, wzrost, plec="k"):
        """
        Metoda inicjalizująca (konstruktor)
        :param imie:
        :param wiek:
        :param wzrost:
        :param plec:
        """
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    # self - obiekt klasy
    def powitanie(self):
        print(f"Nazywam sie: {self.imie}")
        # print(f"Nazywam sie: {cz1.imie}")
        # print(f"Nazywam sie: {cz2.imie}")

    # wypisz_wiek()
    def wypisz_wiek(self):
        print(f"Mam {self.wiek} lat.")

    def wypisz_wzrost(self):
        print(f"Mam {self.wzrost} cm wzrostu.")

    def ruszaj(self):
        if self.plec == "m":
            print(f"Ruszyłem w drogę. [{self.imie}]")
        else:
            print(f"Ruszyłam w drogę. [{self.imie}]")


# TypeError: Human.__init__() missing 3 required positional arguments: 'imie', 'wiek', and 'wzrost'
# cz1 = Human()

cz1 = Human("Radek", 56, 180, "m")
print(cz1.imie)
print(cz1.wiek)
print(cz1.wzrost)
print(cz1.plec)
# Radek
# 56
# 180
# m

cz1.powitanie()
# Nazywam sie: Radek
cz1.wypisz_wiek()  # Mam 56 lat.
print(cz1.__doc__)
# Klasa Human opisująca człowieka w pythonie

cz2 = Human("Anna", 34, 167)
print(cz2.imie)
print(cz2.wiek)
print(cz2.wzrost)
print(cz2.plec)
# Anna
# 34
# 167
# k

cz1.ruszaj()
cz2.ruszaj()
# Ruszyłem w drogę. [Radek]
# Ruszyłam w drogę. [Anna]

cz1.wypisz_wzrost()
cz2.wypisz_wzrost()
# Mam 180 cm wzrostu.
# Mam 167 cm wzrostu.
