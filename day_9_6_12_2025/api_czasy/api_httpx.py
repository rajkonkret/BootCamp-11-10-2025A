import time
import httpx
import asyncio

url = "https://api.nbp.pl/api/exchangerates/rates/A/EUR/"

async def fetch_data(client, url, index):
    start_time = time.time()
    response = await client.get(url)
    elapsed_time = time.time() - start_time
    print(f"Request: {index}: Status {response.status.code}, Time: {elapsed_time}")

