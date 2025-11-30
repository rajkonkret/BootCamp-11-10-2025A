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

# CRUD
# Działanie	        Instrukcja SQL      	HTTP	        DDS
# Create	        INSERT	            PUT / POST	        write
# Read (Retrieve)	SELECT	            GET	                read / take
# Update	        UPDATE	            POST / PUT / PATCH	write
# Delete (Destroy)	DELETE	            DELETE	            dispose
import requests  # klient http

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
