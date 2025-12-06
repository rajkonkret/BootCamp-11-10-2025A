import requests

API_KEY = ""

url = f"https://api.openweathermap.org/data/2.5/weather?q=Warszawa&appid={API_KEY}"
print(url)
page = requests.get(url)
print(page)
print(page.text)
