# pliki csv - dane oddzielone znakiem podziału, pliki tekstowe
# ,;tab
# Kowalski,Jan,Kłodzko
# Nowak,Zenon,Szczecin
# Brzęczyszczykiewicz,Grzegorz,Chrząszczyżewoszyce
import csv  # biblioteka do działań z plikami csv
from datetime import date, datetime, timedelta

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

print("----- Discount -----")

today = date.today()
tomorrow = today + timedelta(days=1)

products = [
    {"sku": 1, 'exp_date': tomorrow, "price": 100},
    {"sku": 2, 'exp_date': today, "price": 200},
    {"sku": 3, 'exp_date': tomorrow, "price": 50.00},
    {"sku": 4, 'exp_date': today, "price": 149.99},
    {"sku": 5, 'exp_date': today, "price": 75},
]

# wyciągnięcie kluczy ze słownika, umieszczonego w liście
fields_product = [k for k in products[0]]

with open("dane/records_discount.csv", "w", newline="") as f:
    csv_dict_writer = csv.DictWriter(f, fieldnames=fields_product)
    csv_dict_writer.writeheader()  # zapisz nazwy kolumn
    csv_dict_writer.writerows(products)  # writerows - zapis listy
