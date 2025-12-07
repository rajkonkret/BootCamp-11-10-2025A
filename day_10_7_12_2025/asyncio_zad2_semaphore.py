import asyncio
import httpx

url = "https://naukajava.online"

# tworzymy semafor - dzieli zadanie na paczki
sema = asyncio.Semaphore(100)


async def fetch(client, i):
    async with sema:
        resp = await client.get(url)


async def main():
    async with httpx.AsyncClient() as client:
        tasks = [fetch(client, i) for i in range(1000)]
        await asyncio.gather(*tasks)


asyncio.run(main())
# (.venv) radoslawjaniak@mac day_10_7_12_2025 % time python asyncio_zad2_semaphore.py
# python asyncio_zad2_semaphore.py  3.19s user 0.70s system 67% cpu 5.801 total dla 500
# python asyncio_zad2_semaphore.py  0.67s user 0.13s system 83% cpu 0.962 total dla 100
