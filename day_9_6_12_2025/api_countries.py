from typing import List

import requests
from pydantic import BaseModel

url = "https://restcountries.com/v3.1/name/Poland"

response = requests.get(url)
# print(response.text)

data = response.json()  # zamiana na słownik
print(type(data))  # <class 'list'>
# print(data[0])

country = data[0]
print(f"Nazwa kraju: {country['name']}")
# Nazwa kraju: {'common': 'Poland', 'official': 'Republic of Poland',
# 'nativeName': {'pol': {'official': 'Rzeczpospolita Polska', 'common': 'Polska'}}}

print(f"Nazwa główna: {country['name']['common']}")  # Nazwa główna: Poland
print(f"Nazwa oficjalna: {country['name']['official']}")  # Nazwa oficjalna: Republic of Poland

# stolica kraju
# populacja

print(f"Stolica kraju: {country['capital']}")  # Stolica kraju: ['Warsaw']
print(f"Stolica kraju: {country['capital'][0]}")  # Stolica kraju: Warsaw

print(f"Liczba ludności: {country['population']}")  # Liczba ludności: 37392000


class Pol(BaseModel):
    official: str
    common: str


class NativeName(BaseModel):
    pol: Pol


class Name(BaseModel):
    common: str
    official: str
    nativeName: NativeName


class CountryInfo(BaseModel):
    name: Name
    capital: List[str]
    population: int


country_data = [CountryInfo(**data) for data in response.json()]

for country in country_data:
    print(country)
# name=Name(common='Poland', official='Republic of Poland',
# nativeName=NativeName(
# pol=Pol(
# official='Rzeczpospolita Polska',
# common='Polska')))
# capital=['Warsaw'] population=37392000

print(type(country))  # <class '__main__.CountryInfo'>
print(country.name)
print(country.name.common)
print(country.name.official)
# Poland
# Republic of Poland

print(country.population)  # 37392000

print(country.capital)
print(country.capital[0])
# ['Warsaw']
# Warsaw

print(country.name.nativeName)
print(country.name.nativeName.pol)
# official='Rzeczpospolita Polska' common='Polska'

print(country.name.nativeName.pol.common)
print(type(country.name.nativeName.pol.common))
# Polska
# <class 'str'>
