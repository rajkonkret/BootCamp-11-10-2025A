import asyncio
import httpx

url = "https://naukajava.online"


async def fetch(client, i):
    resp = await client.get(url)


async def main():
    async with httpx.AsyncClient() as client:
        tasks = [fetch(client, i) for i in range(100)]
        await asyncio.gather(*tasks)


asyncio.run(main())
# cd .. - wyjscie do wyższego katalogu
# cd day_10_7_12_2025 - wejście do katalogu

# (.venv) radoslawjaniak@mac day_10_7_12_2025 % time python asyncio_zad1.py
# python asyncio_zad1.py  0.79s user 0.18s system 87% cpu 1.104 total
# (.venv) radoslawjaniak@mac day_10_7_12_2025 %
# Measure-Command {python asyncio_zad1.py }