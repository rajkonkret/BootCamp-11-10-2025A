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

rates = root.findall(".//Rate")
print(f"Rates: {rates}")  # Rates: [<Element 'Rate' at 0x108f88fe0>, ...

for rate in rates:
    # print(rate)
    currency = rate.find("Currency").text
    code = rate.find("Code").text
    mid = rate.find("Mid").text

    print(f"{code} : {currency} - {mid}")
    # THB : bat (Tajlandia) - 0.1140
    # USD : dolar amerykański - 3.6313
    # AUD : dolar australijski - 2.4079
    # HKD : dolar Hongkongu - 0.4665
    # CAD : dolar kanadyjski - 2.6043

# pip install pydantic-xml
from pydantic_xml import BaseXmlModel, element
from typing import List


class Rate(BaseXmlModel, tag="Rate"):
    Currency: str = element()
    Code: str = element()
    Mid: float = element()


class ExchangeRatesTable(BaseXmlModel, tag="ExchangeRatesTable"):
    Table: str = element()
    No: str = element()
    EffectiveDate: str = element()
    Rates: List[Rate] = element(tag="Rate", path="Rates")


class NBPResponse(BaseXmlModel, tag="ArrayOfExchangeRatesTable"):
    ArrayOfExchangeRatesTable: List[ExchangeRatesTable] = element(tag="ExchangeRatesTable")

# print(response.text)