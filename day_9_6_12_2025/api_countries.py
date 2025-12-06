import requests

url = "https://restcountries.com/v3.1/name/Poland"

response = requests.get(url)
# print(response.text)

data = response.json() # zamiana na słownik
print(type(data)) # <class 'list'>
# print(data[0])

country = data[0]
print(f"Nazwa kraju: {country['name']}")
# Nazwa kraju: {'common': 'Poland', 'official': 'Republic of Poland',
# 'nativeName': {'pol': {'official': 'Rzeczpospolita Polska', 'common': 'Polska'}}}

print(f"Nazwa główna: {country['name']['common']}") # Nazwa główna: Poland
print(f"Nazwa oficjalna: {country['name']['official']}") # Nazwa oficjalna: Republic of Poland

# stolica kraju
# populacja