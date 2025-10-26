with open("test.log", "r") as file:
    lines = file.read()
print(lines)
# Radek
# Kolejna linia
# Jescze jedna
# Nowe dane
# Kolejna linia
# Dopisane2
# Dośdane

with open("test.log", "r", encoding="utf-8") as file:
    lines = file.read()
print(lines)
