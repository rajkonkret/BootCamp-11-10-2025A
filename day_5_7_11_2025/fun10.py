from functools import reduce, lru_cache


def add(a, b):
    return a + b


# For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
#     calculates ((((1 + 2) + 3) + 4) + 5).
sum_all = reduce(add, [1, 2, 3])
print(f"Reduce [sum_all]: {sum_all}")  # Reduce [sum_all]: 6

sum_all = reduce(lambda a, b: a + b, [1, 2, 3])
print(f"Reduce [sum_all]: {sum_all}")  # Reduce [sum_all]: 6 -> (1 + 2) +3) = 6

product = reduce(lambda a, b: a * b, [1, 2, 3, 4])
print(f"Reduce [product]: {product}")  # Reduce [product]: 24

lista = [1, 2, 3, 45, 67, 78, 100, 200, 300]
sum_all = reduce(lambda a, b: a + b, list(map(lambda n: n * 2, list(filter(lambda n: n % 2 == 0, lista)))))
print("Reduce:", sum_all)  # Reduce: 1360

l_1 = [i for i in lista if i % 2 == 0]
l_2 = [i * 2 for i in l_1]
sum_all = reduce(lambda a, b: a + b, l_2)
print(sum_all)  # 1360
