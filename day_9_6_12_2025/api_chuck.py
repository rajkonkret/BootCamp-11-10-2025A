# skorzystac z api chuck norris
# https://api.chucknorris.io/

import requests

url = "https://api.chucknorris.io/jokes/random"

response = requests.get(url)

print(response.text)
data = response.json()

print(data)

print(data.keys())
# dict_keys(['categories', 'created_at', 'icon_url', 'id', 'updated_at', 'url', 'value'])
