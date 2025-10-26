# napisac program kalkulator z wykorzstaniem pętli while
# przechwycic i obsłużyc wyjątki
# ładnie wypisać wynik np.: Dodawaniw 2 + 2 = 4

# wyświetlić menu z działaniami
# pobrac dane
# wyświetlić wynik wybranego działania

while True:
    print("""
    1. Dodawanie
    2. Odejmowanie
    3. Mnożenie
    4. Dzielenie
    5. Koniec
    """)

    odp = input("Podaj opcję menu")
    if odp not in ["1", "2", "3", "4"]:
        break
    try:
        a = float(input("Podaj lizbę a:"))
        b = float(input("Podaj lizbę b:"))

        if odp == "1":
            print(f"Wynik dodawania {a} + {b} = {a + b}")
        elif odp == "2":
            print(f"Wynik odejmowania {a} - {b} = {a - b}")
        elif odp == "3":
            print(f"Wynik mnożenia {a} * {b} = {a * b}")
        elif odp == "4":
            print(f"Wynik dzielenia {a} / {b} = {a / b}")
    except ZeroDivisionError:
        print("Dzielenie przez Zero!!")
    except ValueError:
        print("Bład wartości")
    except Exception as e:
        print("Błąd:", e)
    finally:
        print("Operacja zakończona")
