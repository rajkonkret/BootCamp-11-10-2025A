import requests

access_token = ""
api_url = "https://api.dribbble.com/v2/user"
headers = {"Authorization": f"Bearer {access_token}"}

response = requests.get(api_url, headers=headers)

if response.status_code == 200:
    user_data = response.json()
    print(user_data)
    print(f"Zalogowany jako: {user_data['name']}")
else:
    print('Bład w zapytaniu:', response.json())
