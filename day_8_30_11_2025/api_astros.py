# REST API (Representational State Transfer Application Programming Interface) to styl
# architektury do budowy usług internetowych,
# który określa zestaw zasad komunikacji między różnymi systemami komputerowymi przez internet
# klient - serwer
# klient: przeglądarka
# serwer tzw: backend - serwer który zawiera , przetwarza, odsyłą dane
# GET, POST, PUT/PATCH, DELETE - metody http
# GET - pobiera dane (read)
# POST - wysyła dane (tworzy obiekt) (write)
# PUT/PATCH - aktualizacja obiektu (append)
# DELETE - kasowane (kasowanie)
from typing import List

# CRUD
# Działanie	        Instrukcja SQL      	HTTP	        DDS
# Create	        INSERT	            PUT / POST	        write
# Read (Retrieve)	SELECT	            GET	                read / take
# Update	        UPDATE	            POST / PUT / PATCH	write
# Delete (Destroy)	DELETE	            DELETE	            dispose
import requests  # klient http
from pydantic import BaseModel

# pip install pydantic
# pip install requests
# http://open-notify.org/Open-Notify-API/People-In-Space/

url = "http://api.open-notify.org/astros.json"

response = requests.get(url)
print(response)  # <Response [200]>
# https://pl.wikipedia.org/wiki/Kod_odpowiedzi_HTTP
# statusy odpowiedzi http:
# 2xx - ok
# 3xx - warningi, przekirownanie
# 4xx, 404 - błedny adres url, 400 Bad Request - bład parametrów
# 5xx błedy po stronie serwera, 500 Internal Server Error

print(response.text)
print(type(response.text))  # <class 'str'>

# zamiana jsona na słownik
response_data = response.json()
print(response_data)
print(type(response_data))  # <class 'dict'>

# wypisanie kluczy ze słownika
print(response_data.keys())  # dict_keys(['people', 'number', 'message'])

for k in response_data:
    print(k)
# people
# number
# message

people_list = response_data['people']
print(people_list)
print(type(people_list))  # <class 'list'>

for i in people_list:
    print(i)
# {'craft': 'ISS', 'name': 'Oleg Kononenko'}
# {'craft': 'ISS', 'name': 'Nikolai Chub'}
# {'craft': 'ISS', 'name': 'Tracy Caldwell Dyson'}
# {'craft': 'ISS', 'name': 'Matthew Dominick'}
# {'craft': 'ISS', 'name': 'Michael Barratt'}
# {'craft': 'ISS', 'name': 'Jeanette Epps'}
# {'craft': 'ISS', 'name': 'Alexander Grebenkin'}
# {'craft': 'ISS', 'name': 'Butch Wilmore'}
# {'craft': 'ISS', 'name': 'Sunita Williams'}
# {'craft': 'Tiangong', 'name': 'Li Guangsu'}
# {'craft': 'Tiangong', 'name': 'Li Cong'}
# {'craft': 'Tiangong', 'name': 'Ye Guangfu'}

epps = people_list[5]  # {'craft': 'ISS', 'name': 'Jeanette Epps'}
print(epps)
epps_name = people_list[5]["name"]  # {'craft': 'ISS', 'name': 'Jeanette Epps'}
print(epps_name)  # Jeanette Epps


class Astros(BaseModel):
    craft: str
    name: str


class AstroData(BaseModel):
    # people: list
    people: List[Astros]
    # biblioteka sprawdza typy
    number: int
    # number: str
    message: str


data = AstroData(**response_data)
print(data)
# people=[{'craft': 'ISS', 'name': 'Oleg Kononenko'},
# {'craft': 'ISS', 'name': 'Nikolai Chub'},
# {'craft': 'ISS', 'name': 'Tracy Caldwell Dyson'},
# {'craft': 'ISS', 'name': 'Matthew Dominick'},
# {'craft': 'ISS', 'name': 'Michael Barratt'},
# {'craft': 'ISS', 'name': 'Jeanette Epps'},
# {'craft': 'ISS', 'name': 'Alexander Grebenkin'},
# {'craft': 'ISS', 'name': 'Butch Wilmore'},
# {'craft': 'ISS', 'name': 'Sunita Williams'},
# {'craft': 'Tiangong', 'name': 'Li Guangsu'},
# {'craft': 'Tiangong', 'name': 'Li Cong'}, {
# 'craft': 'Tiangong', 'name': 'Ye Guangfu'}]
# number=12
# message='success'

print(data.number)  # 12
print(data.message)  # success
print(data.people)  # lista
# name=, craft=

for p in data.people:
    # print(p)
    # print(type(p))
    print(p.__class__.__name__)
    print(f"{p.name=} {p.craft=}")
# p.name='Matthew Dominick' p.craft='ISS'
