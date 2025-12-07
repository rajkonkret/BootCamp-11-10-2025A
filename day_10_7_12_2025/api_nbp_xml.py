import requests
from xml.etree import ElementTree as ET

url = "https://api.nbp.pl/api/exchangerates/tables/A/?format=xml"

response = requests.get(url)
# print(response.text)

xml_data = response.content

root = ET.fromstring(xml_data)
print(root)  # <Element 'ArrayOfExchangeRatesTable' at 0x106708db0>

table_name = root.find(".//Table").text
print(f"Tabela: {table_name}")  # Tabela: A

date = root.find(".//EffectiveDate").text
print(f"Data tabeli: {date}")  # Data tabeli: 2025-12-05

no = root.find(".//No").text
print(f"Numer tabeli: {no}")  # Numer tabeli: 236/A/NBP/2025
