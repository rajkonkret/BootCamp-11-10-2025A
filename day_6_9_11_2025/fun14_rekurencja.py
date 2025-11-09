# funkcja rekurencyjna
# funkcj awywołuje samą siebie
# zalety - kompaktowy zapis
# wady - zużycie pamięci, trudny w debugowaniu
def add(num):
    if num == 0:
        return 0
    else:
        return num + add(num - 1)


print(add(5))  # 15 5 + 4 + 3 + 2 + 1


def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num - 1)


print(factorial(5))  # 120


def nwd(a, b):
    if b == 0:
        return a
    else:
        return nwd(b, a % b)


# klasyczne podejscie bez rekurencj
# def nwd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a

print(nwd(48, 18))  # 6
print(48 % 18)  # 12
print(18 % 12)  # 6
print(12 % 6)  # 0 -> więc 6 jest wynikiem tej operacji
