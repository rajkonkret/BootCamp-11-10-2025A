import time
import requests


url = "https://api.nbp.pl/api/exchangerates/rates/A/EUR/"

def multiple_requests():
    start_time = time.time()
    for _ in range(1):
        r = requests.get(url)

    elapsed_time = time.time() - start_time
    print(f"Requests time: {elapsed_time}")


multiple_requests()