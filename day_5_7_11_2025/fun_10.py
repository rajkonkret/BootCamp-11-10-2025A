from functools import reduce, lru_cache


def add(a, b):
    return a + b


# For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
#     calculates ((((1 + 2) + 3) + 4) + 5).
sum_all = reduce(add, [1, 2, 3])
print(f"Reduce [sum_all]: {sum_all}")  # Reduce [sum_all]: 6


