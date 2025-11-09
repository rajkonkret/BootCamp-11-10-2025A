import operator
import time
from functools import partial

import numpy as np  # alias


# pip install numpy

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        exexution_time = end_time - start_time
        print(f"Czas wykonania funkcji: {func.__name__}: {exexution_time}")
        return result

    return wrapper


@measure_time
def my_wait():
    time.sleep(3)  # zatrzymuje dziłanie programu na 3 sek


@measure_time
def my_sum_for():
    suma = 0
    for i in range(15_000_000):
        suma += i
    print("Sum is:", suma)


@measure_time
def my_sum_without_for():
    total = sum(range(15_000_000))
    print("Sum is:", total)


@measure_time
def my_sum_np():
    total = np.sum(np.arange(15_000_000), dtype=np.int64)
    print("Sum is:", total)


print("Start pomiarów:")
# my_wait()  # Czas wykonania funkcji: my_wait: 3.0027430057525635
my_sum_for()  # Czas wykonania funkcji: my_sum_for: 0.9032132625579834
my_sum_without_for()  # Czas wykonania funkcji: my_sum_without_for: 0.3010828495025635
my_sum_np()  # Czas wykonania funkcji: my_sum_np: 0.0348658561706543

lista = list(range(1_000_000))  # lista pythonowa


# lista = list(range(50_000_000))  # lista pythonowa


@measure_time
def my_for_mul():
    l = []
    for i in lista:
        l.append(i * 2)


@measure_time
def my_for_list_compr():
    l1 = [i * 2 for i in lista]


@measure_time
def my_with_map_mul():
    l_map = list(map(lambda x: x * 2, lista))


@measure_time
def my_map_operator():
    l_map = list(map(partial(operator.mul, 2), lista))


arr = np.array(lista)


@measure_time
def my_operator_np():
    return arr * 2


print("----- Część druga (mnożenie listy) -----")
my_for_mul()  # Czas wykonania funkcji: my_for_mul: 0.07256317138671875
my_for_list_compr()  # Czas wykonania funkcji: my_for_list_compr: 0.05586504936218262
my_with_map_mul()  # Czas wykonania funkcji: my_with_map_mul: 0.08725094795227051
my_map_operator()  # Czas wykonania funkcji: my_map_operator: 0.06195211410522461
my_operator_np()  # Czas wykonania funkcji: my_operator_np: 0.0012238025665283203
