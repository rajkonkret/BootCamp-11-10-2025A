# zrobic funkcję restauracja()
# zamow_pizza, zamow_napoj
# w zaleznosci od zamówienia ma zwrocic odpowiednią funkcję
# użyc tych funkcji w programie

def restauracja(typ_zamowienia):
    print("Witamy w naszej restauracji")

    def zamow_pizza(skladniki="pieczarki"):
        # pass
        print("Zamowienie pizza, składniki:", skladniki)

    def zamow_napoj(nazwa="herbata"):
        print("Zamów napoj:", nazwa)

    if typ_zamowienia.casefold().strip() == "pizza":
        return zamow_pizza
    else:
        return zamow_napoj


zamowienie_pizza = restauracja("pizza")
zamowienie_pizza()

zamowienie_pizza("szynka")
# Witamy w naszej restauracji
# Zamowienie pizza, składniki: pieczarki
# Zamowienie pizza, składniki: szynka

zamowienie_napoj = restauracja("napoj")
zamowienie_napoj()
zamowienie_napoj("kawa")
# Witamy w naszej restauracji
# Zamów napoj: herbata
# Zamów napoj: kawa

zamowienie_napoj()
zamowienie_pizza()
zamowienie_napoj()
# Zamów napoj: herbata
# Zamowienie pizza, składniki: pieczarki
# Zamów napoj: herbata
