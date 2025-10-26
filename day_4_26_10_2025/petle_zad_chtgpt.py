# 🧮 Prosty kalkulator z pętlą while, match-case i obsługą wyjątków

while True:
    print("\n=== 🧮 Kalkulator Python ===")
    print("1. Dodawanie (+)")
    print("2. Odejmowanie (-)")
    print("3. Mnożenie (*)")
    print("4. Dzielenie (/)")
    print("5. Wyjście (q)")

    choice = input("Wybierz działanie (1-5 lub q): ").strip()

    # 💡 Możliwość zakończenia programu
    if choice.lower() in ("5", "q", "quit", "exit"):
        print("👋 Zakończono działanie kalkulatora.")
        break

    try:
        # 🧩 Pobieranie danych wejściowych
        a = float(input("Podaj pierwszą liczbę: "))
        b = float(input("Podaj drugą liczbę: "))

        # ⚙️ Match-case – rozpoznawanie wyboru użytkownika
        match choice:
            case "1" | "+":
                result = a + b
                operation = "Dodawanie"
            case "2" | "-":
                result = a - b
                operation = "Odejmowanie"
            case "3" | "*":
                result = a * b
                operation = "Mnożenie"
            case "4" | "/":
                # 🚫 Obsługa dzielenia przez zero
                if b == 0:
                    raise ZeroDivisionError("Nie można dzielić przez zero!")
                result = a / b
                operation = "Dzielenie"
            case _:
                print("⚠️ Nieznane działanie. Spróbuj ponownie.")
                continue  # wróć do początku pętli

        # 🎯 Ładne wypisanie wyniku
        print(f"\n✅ {operation}: {a} i {b}")
        print(f"➡️ Wynik: {a} {choice} {b} = {result}\n")

    except ValueError:
        # Obsługa błędów konwersji na float
        print("❌ Błąd: podano nieprawidłową liczbę.")
    except ZeroDivisionError as e:
        # Obsługa dzielenia przez zero
        print(f"❌ Błąd: {e}")
    except Exception as e:
        # Każdy inny, niespodziewany wyjątek
        print(f"⚠️ Wystąpił nieoczekiwany błąd: {e}")