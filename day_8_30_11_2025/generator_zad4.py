# stworzenie raportu
# generator do wygenerowanie danych
# przetworzenie danych
# dekorator do pomiatu czasu
import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        exexution_time = end_time - start_time
        print(f"Czas wykonania funkcji: {func.__name__}: {exexution_time}")
        return result

    return wrapper
