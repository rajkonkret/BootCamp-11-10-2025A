# pętla - możliwość wykonywania tego samego fragmentu kodu wielokrotnie
# for - pętla iteracyjna

for i in range(10):  # od 0 do 9
    print(i)

for i in range(10):
    print(i, i, sep=":")  # 9:9
    print(i, i)  # string inserted between values, default a space, 9 9

for i in range(10):
    print(i, end="")  # 0123456789, standardowo: end='\n'

print("Nowa linia")  # 0123456789Nowa linia
print("Prawdziwa nowa linia")
# 0123456789Nowa linia
# Prawdziwa nowa linia
print()

for i in range(1, 20):  # od 1 do 19
    print(i)

for i in range(5):
    print("Komunikat")

for _ in range(1, 5):  # nie ma zmienna
    print("Komunikat")
    # print(_)
    # Komunikat
    # 4
