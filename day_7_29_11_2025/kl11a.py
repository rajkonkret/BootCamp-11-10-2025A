class MyClassCounter:
    counter = 0

    @classmethod
    def increment_counter(cls):
        cls.counter += 1
        return cls.counter


print(MyClassCounter.increment_counter())
print(MyClassCounter.increment_counter())
print(MyClassCounter.increment_counter())
c = MyClassCounter()
print(c.increment_counter())  # 4


class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    @classmethod
    def from_full_name(cls, full_name):
        imie, nazwisko = full_name.split()
        return cls(imie, nazwisko)


osoba1 = Osoba("Jan", "Kowalski")
print(osoba1.imie, osoba1.nazwisko)
# Jan Kowalski

dane = "Jan Kowalski"
print(dane.split())  # ['Jan', 'Kowalski']
imie, nazwisko = dane.split()
print(imie)
print(nazwisko)
osoba2 = Osoba(imie, nazwisko)
print(osoba2.imie, osoba2.nazwisko)  # Jan Kowalski

osoba3 = Osoba.from_full_name(dane)
print(osoba3.imie)
print(osoba3.nazwisko)
# Jan
# Kowalski
