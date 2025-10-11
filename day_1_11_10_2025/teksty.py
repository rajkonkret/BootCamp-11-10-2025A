tekst = "Witaj Świecie"

print(tekst)
print(type(tekst))
# Witaj Świecie
# <class 'str'>

# pula tekstów - teksty niemutowalne
tekst.upper()
#    """ Return a copy of the string converted to uppercase. """
print(tekst)  # Witaj Świecie
print(tekst.upper())  # WITAJ ŚWIECIE
print(tekst)  # Witaj Świecie
tekst_upper = tekst.upper()
print(tekst_upper)  # WITAJ ŚWIECIE

assert tekst_upper == "WITAJ ŚWIECIE"  # asercja, sprawdzenie czy zmmienna zawiera wskazaną wartość

print(tekst.lower())  # witaj świecie
print(tekst.capitalize())  # Witaj świecie


