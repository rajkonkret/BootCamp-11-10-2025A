# od python 3.10 istnieje match case

# lista = []
# lang = input("Podaj znany Ci język programowania")
#
# match lang.casefold().strip():
#     case "python":
#         print("Lubie Pythona")
#         lista.append(lang.capitalize())
#     case "java":
#         print("Java to kawa")
#         lista.append(lang.capitalize())
#     case "c++":
#         print("To za trudne")
#         lista.append(lang.capitalize())
#     case _:  # odpowiednik else
#         print("Nie znam takiego języka")
#
# print(f"Lista z odpowiedziami: {lista}")
# # Podaj znany Ci język programowaniajava
# # Java to kawa
# # Lista z odpowiedziami: ['Java']

dane = [1, 2, 3]
# dane = {"nazwa": "Radek", "wiek": 45}

match dane:
    case [a, b, c]:
        print(f"Lista z trzema elementami: {a=}, {b=}, {c=}")
    case {'nazwa': n, "wiek": w}:
        print(f"Słownik reprezentujący osobę: {n}, wiek: {w}")
    case _:
        print("Błędny typ danych")
# Słownik reprezentujący osobę: Radek, wiek: 45
# Lista z trzema elementami: a=1, b=2, c=3
