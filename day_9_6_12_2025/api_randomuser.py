import requests
from pydantic import BaseModel

url = "https://randomuser.me/api/"

response = requests.get(url)
print(response)

print(response.text)

data = response.json()

user = data['results'][0]
print(user)

print(f"Osoba: {user['name']}")
# Osoba: {'title': 'Mr', 'first': 'David', 'last': 'Harris'}
print(f"Imię: {user['name']['first']}")  # Imię: David
print(f"Nazwisko: {user['name']['last']}")  # Nazwisko: Harris

print(f"Numer telefonu: {user['phone']}")  # Numer telefonu: (664) 429 3469

# "picture": {
#         "large": "https://randomuser.me/api/portraits/women/3.jpg",
#         "medium": "https://randomuser.me/api/portraits/med/women/3.jpg",
#         "thumbnail": "https://randomuser.me/api/portraits/thumb/women/3.jpg"
#       }

user_name = user['name']['first']
user_last_name = user['name']['last']

photo_url = user['picture']['large']
print(f"Link do zdjęcia: {photo_url}")

response_photo = requests.get(photo_url)
print(response_photo)

filename = f"{user_name.lower()}_{user_last_name.lower()}.jpg"
with open(filename, "wb") as f:  # "wb" zapis bajtowy
    f.write(response_photo.content)

print("Zdjęcie zostało zapisane:", filename)
