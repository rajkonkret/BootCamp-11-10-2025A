# od python 3.10 istnieje match case

lista = []
lang = input("Podaj znany Ci język programowania")

match lang.casefold().strip():
    case "python":
        print("Lubie Pythona")
        lista.append(lang.capitalize())
    case "java":
        print("Java to kawa")
        lista.append(lang.capitalize())
    case "c++":
        print("To za trudne")
        lista.append(lang.capitalize())
    case _:  # odpowiednik else
        print("Nie znam takiego języka")

print(f"Lista z odpowiedziami: {lista}")
# Podaj znany Ci język programowaniajava
# Java to kawa
# Lista z odpowiedziami: ['Java']
