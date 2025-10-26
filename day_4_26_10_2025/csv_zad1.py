# pliki csv - dane oddzielone znakiem podziału, pliki tekstowe
# ,;tab
# Kowalski,Jan,Kłodzko
# Nowak,Zenon,Szczecin
# Brzęczyszczykiewicz,Grzegorz,Chrząszczyżewoszyce
import csv  # biblioteka do działań z plikami csv

fields = ['name', 'branch', 'year', 'cgpa']
row = ["Radek", "Coe", "3", 0]

zipped_dict = dict(zip(fields, row))
print(zipped_dict)
# {'name': 'Radek', 'branch': 'Coe', 'year': '3', 'cgpa': 0}

# newline="" - obejscie problemu ppustych linii
# zapis do pliku csv
with open("dane/records.csv", "w", newline="") as csv_f:
    csvwriter = csv.writer(csv_f)  # narzedzie do zapisu do pliku csv
    csvwriter.writerow(row)

with open("dane/records_2.csv", "w", newline="") as csv_f:
    csvwriter = csv.writer(csv_f)  # narzedzie do zapisu do pliku csv
    csvwriter.writerow(fields)
    csvwriter.writerow(row)

with open("dane/records_3.csv", "w", newline="") as f:
    csv_dict_writer = csv.DictWriter(f, fieldnames=fields)
    csv_dict_writer.writeheader()  # zapisz nazwy kolumn
    csv_dict_writer.writerow(zipped_dict)
