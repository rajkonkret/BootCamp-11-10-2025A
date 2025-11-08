import csv

columns = []
rows = []

# filename = 'dane/records_3.csv'  # wile wierszy
filename = 'dane/records_discount.csv'  # wile wierszy

with open(filename, "r") as f:
    dialect = csv.Sniffer().sniff(f.read(1024))  # wczytujemy 1024 znaki
    print(dialect.delimiter)  # ";"
    f.seek(0)  # ustawienie odczytu na początek pliku

    # csvreader = csv.reader(f)
    # csvreader = csv.reader(f, delimiter=";")
    csvreader = csv.reader(f, delimiter=dialect.delimiter)

    print(csvreader)  # <_csv.reader object at 0x102b855b0>
    # iterator - można go używac sekwencyjnie
    # pobrac po kolei pojedyncze elemnty next()
    # StopIteration - wyczerpanie danych z iteratora
    columns = next(csvreader)  # pierwszy wiersz, wskażnik ustawiony na drugi

    for row in csvreader:  # zacznie od wiersza drugiego
        # print(row)
        rows.append(row)

print("Columns:", columns)
print("Rows:", rows)
# Columns: ['name', 'branch', 'year', 'cgpa']
# Rows: [['Radek', 'Coe', '3', '0']]

# plik discount
# Columns: ['sku;exp_date;price']
# Rows: [['1;2025-11-09;100'],
# ['2;2025-11-08;200'],
# ['3;2025-11-09;50.0'],
# ['4;2025-11-08;149.99'],
# ['5;2025-11-08;75']]

# delimiter=";"
# Columns: ['sku', 'exp_date', 'price']
# Rows: [['1', '2025-11-09', '100'],
# ['2', '2025-11-08', '200'],
# ['3', '2025-11-09', '50.0'],
# ['4', '2025-11-08', '149.99'],
# ['5', '2025-11-08', '75']]
