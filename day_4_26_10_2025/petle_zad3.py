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

password = input("Podaj hasło")
while password != 'secret':
    password = input("Błędne hasło. Podaj ponownie")
print("Hasło prawidłowe")
# Podaj hasłoassasa
# Błędne hasło. Podaj ponownieasasa
# Błędne hasło. Podaj ponowniewer
# Błędne hasło. Podaj ponownienmbm
# Błędne hasło. Podaj ponowniedvxcvc
# Błędne hasło. Podaj ponowniezcxvz
# Błędne hasło. Podaj ponowniesecret
# Hasło prawidłowe


