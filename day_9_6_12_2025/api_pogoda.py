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
