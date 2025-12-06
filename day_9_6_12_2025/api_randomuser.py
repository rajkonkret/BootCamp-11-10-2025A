import requests
from pydantic import BaseModel, HttpUrl, EmailStr

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

filename = f"pictures/{user_name.lower()}_{user_last_name.lower()}.jpg"
with open(filename, "wb") as f:  # "wb" zapis bajtowy
    f.write(response_photo.content)

print("Zdjęcie zostało zapisane:", filename)


class Name(BaseModel):
    title: str
    first: str
    last: str


class Picture(BaseModel):
    large: HttpUrl
    medium: HttpUrl
    thumbnail: HttpUrl


class UserInfo(BaseModel):
    name: Name
    # email: str
    email: EmailStr
    picture: Picture


user = data['results'][0]
user_info = UserInfo(**user)
print(user_info)

print(f"Imię: {user_info.name.first}")
print(f"Nazwisko: {user_info.name.last}")
# Imię: Dean
# Nazwisko: Fernandez

print(f'Email: {user_info.email}')
# Email: linnea.suomi@example.com

# pip install email-validator

photo_url_pydantic = user_info.picture.large
print(f"link do zdjęcia: {photo_url_pydantic}")

# str() - rzutowanie na string
response_photo_pydantic = requests.get(str(photo_url_pydantic))
print(response_photo_pydantic)

filename = f"pictures/pydantic_{user_name.lower()}_{user_last_name.lower()}.jpg"
with open(filename, "wb") as f:  # "wb" zapis bajtowy
    f.write(response_photo_pydantic.content)

print("Zdjęcie zostało zapisane:", filename)
