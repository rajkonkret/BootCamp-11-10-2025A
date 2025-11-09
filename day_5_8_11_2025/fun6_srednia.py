# funkcja, która oblicza srednią
def srednia(name=None, *cyfry):  # * dowolna ilośc argumentów pozycyjnych
    print(cyfry)
    count = len(cyfry)
    suma = 0
    sum_p = sum(cyfry)
    try:
        for c in cyfry:
            suma += c
        avg = suma / count
        avg_p = sum_p / count

    except Exception as e:
        print("Bład:", e)
    else:  # tylko gdy nie ma błedu
        print(f"Średnia dla ucznia: {name} wynosi:  {avg}")
        print(f"Średnia dla ucznia: {name} wynosi:  {avg_p}")
    finally:  # wykona się zawsze
        print("Następny uczeń")


srednia()  # ()
srednia(1)  # (1,)
srednia(1, 2, 3)  # (1, 2, 3)
# ()
# Bład: division by zero
# Następny uczeń
# (1,)
# Średnia wynosi:  1.0
# Następny uczeń
# (1, 2, 3)
# Średnia wynosi:  2.0
# Następny uczeń
srednia("Radek", 6, 6, 6, 6, 6, 5)
# Średnia dla ucznia: Radek wynosi:  5.833333333333333
# Następny uczeń
# Średnia dla ucznia: Radek wynosi:  5.833333333333333
# Średnia dla ucznia: Radek wynosi:  5.833333333333333
# Następny uczeń
