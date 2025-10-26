# pętla while
# sterowana warunkiem

# pętla nieskończona
# while True:
#     print("Komunikat 1 !")

licznik = 0
while True:
    print("Komunikat 2 !!")
    licznik += 1
    if licznik > 15:
        break  # przrywa pętle
print(licznik)  # 16

licznik = 0
while licznik < 15:
    licznik += 1
    print("Komunikat 3 !!!")

# password = input("Podaj hasło")
# while password != 'secret':
#     password = input("Błędne hasło. Podaj ponownie")
# print("Hasło prawidłowe")
# Podaj hasłoassasa
# Błędne hasło. Podaj ponownieasasa
# Błędne hasło. Podaj ponowniewer
# Błędne hasło. Podaj ponownienmbm
# Błędne hasło. Podaj ponowniedvxcvc
# Błędne hasło. Podaj ponowniezcxvz
# Błędne hasło. Podaj ponowniesecret
# Hasło prawidłowe

lista = []
lista_int = []
while True:
    wej = input("Podaj liczbę")  # -> str
    # A string is numeric if all characters in the string are numeric
    if not wej.isnumeric():
        break
    lista.append(wej)
    lista_int.append(int(wej))

print(lista)
print(lista_int)
# Podaj liczbę1
# Podaj liczbę2
# Podaj liczbę3
# Podaj liczbę4
# Podaj liczbę5
# Podaj liczbęa
# ['1', '2', '3', '4', '5']
# Podaj liczbę1
# Podaj liczbę2
# Podaj liczbę3
# Podaj liczbę4
# Podaj liczbę5
# Podaj liczbęa
# ['1', '2', '3', '4', '5'] str
# [1, 2, 3, 4, 5] int

my_list = [1, 5, 2, 3, 5, 4, 5, 6, 5]
element_to_remove = 5
while element_to_remove in my_list:
    my_list.remove(element_to_remove)

print(my_list)  # [1, 2, 3, 4, 6], usunęło zduplikowane elementy nie zmieniająć kolejności
