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
