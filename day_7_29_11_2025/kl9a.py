class Pojazd:
    def serwis(self):
        print("Serwisowanie samochodu")


class SamochodOsobowy(Pojazd):
    def serwis(self):
        print("Serwisowanie samochodu osobowego")


class SamochodDostawczy(Pojazd):
    def serwis(self):
        print("Serwis samochodu dostawczego")


class PojazdSluzbowy(Pojazd):
    def rejestracja_sluzbowa(self):
        print("Rejestracja pojazdu służbowego")


class SamochodsluzbowyOsobowy(SamochodOsobowy, PojazdSluzbowy):
    pass


# class SamochodsluzbowyOsobowy(PojazdSluzbowy, SamochodOsobowy):
#     pass


car1 = SamochodsluzbowyOsobowy()
car1.serwis()
car1.rejestracja_sluzbowa()
# Serwisowanie samochodu osobowego
# Rejestracja pojazdu służbowego

print(SamochodsluzbowyOsobowy.__mro__)
# (<class '__main__.SamochodsluzbowyOsobowy'>, <class '__main__.SamochodOsobowy'>,
# <class '__main__.PojazdSluzbowy'>, <class '__main__.Pojazd'>, <class 'object'>)
