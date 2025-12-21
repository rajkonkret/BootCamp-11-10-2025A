import datetime

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client['przykladowa_baza']
kolekcja = db['uzytkownicy']

kolekcja.insert_one(
    {'imie': "Jan", "nazwisko": "Kowalski", "wiek": 30}
)

client.close()
