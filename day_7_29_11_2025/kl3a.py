class ContactList(list['Contact']):
    """
    Lista z metodą search
    """

    def search(self, name):
        matching_contacts = []
        for c in self:
            if name.casefold() in c.name.casefold():
                matching_contacts.append(c)
        return matching_contacts


class Contact:
    # all_contacts = []  # pusta lista, wspólna dla wszystkich obiektów klasy
    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    # __repr__ rownież zmienia __str__
    # !r - dodaje cudzysłowia do stringów
    def __repr__(self):
        return f"{self.name!r} {self.email!r}"


class Suplier(Contact):
    """
    Klasa Suplier dziedziczy po klasie Contact
    """

    def order(self, order):
        print(f"{order} zamówiono od {self.name}")


# stworzyc klasę Friend dziedziczącą po  Suplier, ma dodakowo przyjmowac numer telefonu
class Friend(Suplier):
    """
    Kalsa dziedziczy po kalsie Suplier
    """

    def __init__(self, name, email, phone="000000000"):
        super().__init__(name, email)
        self.phone = phone

    def __repr__(self):
        return f"{self.__class__.__name__} {self.name!r} {self.email!r} +48{self.phone}"


c1 = Contact("Adam", "adam@wp.pl")
c2 = Contact("Radek", "radek@wp.pl")
c3 = Contact("Tomek", "tomek@wp.pl")

print(c1)  # Adam adam@wp.pl
print(c2)  # Radek radek@wp.pl
print(c3)  # Tomek tomek@wp.pl

print(c1.all_contacts)  # [Adam adam@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl]
print(c2.all_contacts)  # [Adam adam@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl]
print(c3.all_contacts)  # [Adam adam@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl]

# wspolna dla wszystkich obiektów klasy
print(Contact.all_contacts)  # [Adam adam@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl]

s1 = Suplier("Marek", "marek@o2.pl")
print(s1.all_contacts)  # [Adam adam@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl, Marek marek@o2.pl]
print(c1.all_contacts)  # [Adam adam@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl, Marek marek@o2.pl]

s1.order("kawa")  # kawa zamówiono od Marek

# wypisz kontak "Radek" z listy all_contacts
# AttributeError: 'list' object has no attribute 'search'
# c1.all_contacts.search("Radek")

c_l = ContactList()
print(c_l.search("Radek"))  # []
c_l.append(c1)
c_l.append(c2)
c_l.append(c3)
c_l.append(s1)
print(c_l)
# [Adam adam@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl, Marek marek@o2.pl]
print(c_l.search("Radek"))  # [Radek radek@wp.pl]
print(Contact.all_contacts)
# [Adam adam@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl, Marek marek@o2.pl]
