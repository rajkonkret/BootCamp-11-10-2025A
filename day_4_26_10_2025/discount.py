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


