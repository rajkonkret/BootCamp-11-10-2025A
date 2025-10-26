from datetime import date, datetime, timedelta

today = date.today()
print("Dzisiejsza data:", today)  # Dzisiejsza data: 2025-10-26
print(type(today))  # <class 'datetime.date'>

time = datetime.now()
print("Aktualny czas:", time)  # Aktualny czas: 2025-10-26 11:03:52.945877
print(type(time))  # <class 'datetime.datetime'>

print("Godzina:", time.hour)
print("Dzień:", today.day)
# Godzina: 11
# Dzień: 26

formated_date = datetime.now().strftime("%d/%m/%Y")
print("Dzisiejsza data (sformatowana):", formated_date)
# Dzisiejsza data (sformatowana): 26/10/2025
print(type(formated_date))  # <class 'str'>

# 11:07
formated_time = datetime.now().strftime("%H:%M")
print("Aktualna godzina (sformatowana):", formated_time)
# Aktualna godzina (sformatowana): 11:11
print(type(formated_time))  # <class 'str'>
# 09:14 -> 9:14
print("Aktualna godzina (bez zera wiodącego):", formated_time.removeprefix("0"))
# Aktualna godzina (bez zera wiodącego): 11:12

# czas USA
formated_time_usa = datetime.now().strftime("%I:%M %p")
print("Aktualna godzina (sformatowana USA):", formated_time_usa)
# Aktualna godzina (sformatowana USA): 11:13 AM

time_from_str = datetime.now().strptime("26/10/2025", "%d/%m/%Y")
print("Data ze stringa:", time_from_str)  # Data ze stringa: 2025-10-26 00:00:00
print(type(time_from_str))  # <class 'datetime.datetime'>

# tomorrow = today + 1  # TypeError: unsupported operand type(s) for +: 'datetime.date' and 'int'
# days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0
tomorrow = today + timedelta(days=1)
print("Jutro będzie:", tomorrow)  # Jutro będzie: 2025-10-27

print("----- Discount -----")
products = [
    {"sku": 1, 'exp_date': tomorrow, "price": 100},
    {"sku": 2, 'exp_date': today, "price": 200},
    {"sku": 3, 'exp_date': tomorrow, "price": 50.00},
    {"sku": 4, 'exp_date': today, "price": 149.99},
    {"sku": 5, 'exp_date': today, "price": 75},
]

for product in products:
    # print(product)  # {'sku': 1, 'exp_date': datetime.date(2025, 10, 26), 'price': 100}
    # print(product['exp_date'])  # 2025-10-26

    # if product['exp_date'] == today:
    if product['exp_date'] != today:
        continue
        # kończy bieżące wykonanie pętli, nakazuje pobrać kolejny element
    product['price'] *= 0.8  # price = price * 0.2
    print(f"""Price for dku: {product['sku']}, date: {product['exp_date']}
is now: {product['price']}""")
# ----- Discount -----
# Price for dku: 1, date: 2025-10-26
# is now: 80.0
# Price for dku: 2, date: 2025-10-26
# is now: 160.0
# Price for dku: 4, date: 2025-10-26
# is now: 119.99200000000002
# Price for dku: 5, date: 2025-10-26
# is now: 60.0
# Wariant 2
# ----- Discount -----
# Price for dku: 2, date: 2025-10-26
# is now: 160.0
# Price for dku: 4, date: 2025-10-26
# is now: 119.99200000000002
# Price for dku: 5, date: 2025-10-26
# is now: 60.0
