from datetime import datetime

import requests

API_KEY = ""

url = f"https://api.openweathermap.org/data/2.5/weather?q=Warszawa&appid={API_KEY}&lang=pl&units=metric&format=json"
print(url)
page = requests.get(url)
print(page)
print(page.text)

data = page.json()
print("Miasto:", data['name'])  # Miasto: Warszawa
print("Miasto:", data['weather'][0]['description'])  # Miasto: zachmurzenie duże
print("Aktualna temperatura:", data['main']['temp'])
print("Aktualna temperatura:", data['main']['temp_min'])
print("Aktualna temperatura:", data['main']['temp_max'])
# Miasto: zachmurzenie duże
# Aktualna temperatura: 7.25
# Aktualna temperatura: 6.47
# Aktualna temperatura: 8.21

print(50 * "-")
sunrise = data['sys']['sunrise']
print("Wschód słońca (timestamp):", sunrise)  # Wschód słońca: 1765002574
# timstamp - liczba sekund od epoki Unixa - 1 stycznia 1970 r
dt_object_sunrise = datetime.fromtimestamp(sunrise)  # przeliczenie na datetime
print("Wschód słońca:", dt_object_sunrise)  # Wschód słońca: 2025-12-06 07:29:34

print(50 * "-")
sunset = data['sys']['sunset']
print("Zachód słońca (timestamp):", sunset)  # Wschód słońca: 1765002574
# timstamp - liczba sekund od epoki Unixa - 1 stycznia 1970 r
dt_object_sunset = datetime.fromtimestamp(sunset)  # przeliczenie na datetime
print("Zachód słońca:", dt_object_sunset)  # Wschód słońca: 2025-12-06 07:29:34
# Zachód słońca (timestamp): 1765031085
# Zachód słońca: 2025-12-06 15:24:45
