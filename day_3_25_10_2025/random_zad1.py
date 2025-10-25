import random

# random - działania na liczbach losowych

# """Return random integer in range [a, b], including both end points.
print(random.randint(1, 100))  # int 52 od 1 do 100

print(random.randrange(1, 100))  # 94, int, od 0 do 99
print(random.randrange(5))  # od 0 do 4

print(random.random())  # 0.04727211807938381, float, od 0 do 0.9999999
print(random.random() * 8)  # 1.9207021073560595, float, od 0 do 7.9999999

lista = [5, 7, 45, 34, 56]

index = random.randrange(len(lista))
print(index, lista[index])  # 3 34

print(random.choice(lista))  # losuje element z listy: 45

print("-" * 20)
# bęben maszyby losującej -> lista
# losowanie kul -> random.choice
# usunięcei kuli z bębna -> remove
# wypisanie liczby -> print
lista_kule = list(range(1, 50))  # od 1 do 49
# print(lista_kule)

wyn = random.choice(lista_kule)
print(wyn)
lista_kule.remove(wyn)

print(random.choices(lista_kule, k=6))  # [14, 22, 8, 8, 40, 30], losuje z powtórzeniami
print(random.sample(lista_kule, k=6))  # [33, 7, 45, 39, 35, 40], losowanie bez powtórzeń, [13, 44, 24, 25, 18, 9]
print(random.sample(lista_kule, 6))  # [20, 6, 25, 31, 18, 35], losowanie bez powtórzeń
