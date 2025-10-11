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

name = "Radek"
#       01234 - indeksowannie od zera

print(name[0])  # R
print(name[1])  # a
print(name[2])  # d
print(name[3])  # e
print(name[4])  # k

# print(name[5])  # IndexError: string index out of range - zwraca bład

print(len(name))  # len() - długość ciągu,5

# slicowanie - fragment tekstu
print(name[2:4])  # de, tylko indeksy 2,3 z prawej strony otwarty(niewłącznie)
print(name[:4])  # Rade 0,1,2,3 indeksy
print(name[:])  # Radek

str1 = "HELLO WORLD"
# teksty są niemutowalne!!!
# str1[0:5] = "HOLAA" # TypeError: 'str' object does not support item assignment
print(str1)  # HELLO WORLD

my_str = "   Hello Everyone   "
print(my_str)  # "   Hello Everyone   "
print(my_str.strip())  # "Hello Everyone" - usunięcie białych znaków (spacji) - wiodącę i końcowe
print(my_str.rstrip())  # "   Hello Everyone" - usunięcie z prawej strony
print(my_str.lstrip())  # "Hello Everyone   " - usunięcie z lewej strony

my_str2 = "***Hello****World***"
print(my_str2.strip("*"))  # Hello****World
print(my_str2.rstrip("*"))  # ***Hello****World
print(my_str2.lstrip("*"))  # Hello****World***

print(my_str)  # "   Hello Everyone   "
print(my_str2)  # "***Hello****World***"

print(tekst)  # Witaj Świecie
# Witaj Świecie
# 0123456789012

print(tekst.removeprefix("Witaj"))  # " Świecie"
print(tekst.removesuffix("Świecie"))  # "Witaj "

print(tekst.count("i"))  # występuje 3 razy
print(tekst.count("i", 0, 4))  # występuje 1 raz
print(tekst.count("j", 0, 4))  # występuje 0 razy, bo indeksy 0123

# sprawdzenie indeksu dla danej literki
print(tekst.index("j"))  # indeks numer: 4

print(my_str2)  # ***Hello****World***
# zamiana tekstu
print(my_str2.replace("He", "Ho"))  # ***Hollo****World***

print(my_str)  # "   Hello Everyone   "
print(my_str.replace(" ", ""))  # HelloEveryone
print(my_str.center(40))  # wycentrowanie tekstu podczas wypisywania
# "             Hello Everyone             "

print("Mój ulubiony serial \"Alternatywy 4\"")  # Mój ulubiony serial "Alternatywy 4"
print('Mój ulubiony serial "Alternatywy 4"')  # Mój ulubiony serial "Alternatywy 4"
# \ - w stringach znak ucieczzki, nie interpretuj kolejnoga znaku tylko po prostu wyświetl
