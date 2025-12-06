# https://api.nbp.pl/
# zapytanie o pojedynczą walute. Tabela A
# wypisac nazwę i kurs waluty
# słownikiem
# obiektami
from typing import List

import requests
from pydantic import BaseModel
from datetime import datetime

# https://pl.wikipedia.org/wiki/ISO_4217
url = "https://api.nbp.pl/api/exchangerates/rates/A/EUR/"

response = requests.get(url)

print(response.text)

table = response.json()
print(type(table))
print(table)

print(table['currency'])
print(f"{table.get('rates')}")  # [{'no': '236/A/NBP/2025', 'effectiveDate': '2025-12-05', 'mid': 4.2321}]
print(f"{table.get('rates')[0]['mid']}")  # 4.2321


class Rate(BaseModel):
    no: str
    # effectiveDate: str
    effectiveDate: datetime
    mid: float


class CurrencyData(BaseModel):
    table: str
    currency: str
    code: str
    rates: List[Rate]


currency_data = CurrencyData(**table)
print(currency_data)
# table='A' currency='euro' code='EUR'
# rates=[Rate(no='236/A/NBP/2025', effectiveDate='2025-12-05', mid=4.2321)]

print(currency_data.currency)
print(currency_data.table)
print(currency_data.code)
print(currency_data.rates)
# A
# EUR
# [Rate(no='236/A/NBP/2025', effectiveDate='2025-12-05', mid=4.2321)]

print(currency_data.rates[0])
print(currency_data.rates[0].no)
print(currency_data.rates[0].effectiveDate)
print(currency_data.rates[0].mid)
# 236/A/NBP/2025
# 2025-12-05
# 4.2321

# po zamienie daty str -> datetime
# no='236/A/NBP/2025' effectiveDate=datetime.datetime(2025, 12, 5, 0, 0) mid=4.2321
print(type(currency_data.rates[0].effectiveDate))  # <class 'datetime.datetime'>

effectiveDate = currency_data.rates[0].effectiveDate
formated_date = effectiveDate.strftime("%d/%m/%Y")
print(f"Data tabeli: {formated_date}")  # Data tabeli: 05/12/2025
