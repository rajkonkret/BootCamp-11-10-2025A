class Contact:
    all_contacts = []  # pusta lista, wspólna dla wszystkich obiektów klasy

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    # __repr__ rownież zmienia __str__
    def __repr__(self):
        return f"{self.name} {self.email}"


class Suplier(Contact):
    """
    Klasa Suplier dziedziczy po klasie Contact
    """

    def order(self, order):
        print(f"{order} zamówiono od {self.name}")


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
