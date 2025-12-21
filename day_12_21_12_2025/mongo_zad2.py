import datetime
# https://tableplus.com - gui
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client['przykladowa_baza']
kolekcja = db['uzytkownicy']

# kolekcja.insert_one(
#     {'imie': "Jan", "nazwisko": "Kowalski", "wiek": 30}
# )

kolekcja.insert_many(
    [
        {'imie': "Anna", "nazwisko": "Nowak", "wiek": 27},
        {'imie': "Paweł", "nazwisko": "Wiśniewski", "wiek": 34, "czas": datetime.datetime.now().strftime("%d/%m/%Y")},
    ]
)

for uzytkownik in kolekcja.find():
    print(uzytkownik)
    # {'_id': ObjectId('6947f516ac0a07e131ca6248'), 'imie': 'Jan', 'nazwisko': 'Kowalski', 'wiek': 30}
    print(f"{uzytkownik['imie']}, {uzytkownik['nazwisko']}")
    # Jan, Kowalski

client.close()
# {'_id': ObjectId('6947f821c28ba54c4e9a3dad'), 'imie': 'Anna', 'nazwisko': 'Nowak', 'wiek': 27}
# Anna, Nowak
# {'_id': ObjectId('6947f821c28ba54c4e9a3dae'), 'imie': 'Paweł', 'nazwisko': 'Wiśniewski', 'wiek': 34, 'czas': '21/12/2025'}
# Paweł, Wiśniewski
