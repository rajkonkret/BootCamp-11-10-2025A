import chardet

# pip install chardet
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

file_path = "test.log"
# chardet wymaga by odczytać plik binarnie
with open(file_path, "rb") as file:
    raw_data = file.read()

print(raw_data)
# b'Radek\nKolejna linia\nJescze jedna\nNowe dane\nKolejna linia\nDopisane2\nDo\xc5\x9bdane\n'
# \xc5\x9b - zapis szesnastokowy dla znaku Ś w unicode

result = chardet.detect(raw_data)
print(result)
# {'encoding': 'Windows-1254', 'confidence': 0.6539604138968763, 'language': 'Turkish'}
# Po zwiększeniu próbki, wskazuje poprawnie
# {'encoding': 'utf-8', 'confidence': 0.87625, 'language': ''}
encoding = result['encoding']
confidence = result['confidence']
print("kodowanie znaków:", encoding)
print(f"trafnośc:{confidence * 100:.2f} %")
# kodowanie znaków: utf-8
# trafnośc:87.62 %
print(raw_data.decode(encoding=encoding))
# Radek
# Kolejna linia
# Jescze jedna
# Nowe dane
# Kolejna linia
# Dopisane2
# Dośąźdane
