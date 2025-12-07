import asyncio
import httpx

url = "https://naukajava.online"


async def fetch(client, i):
    resp = await client.get(url)


async def main():
    async with httpx.AsyncClient() as client:
        tasks = [fetch(client, i) for i in range(500)]
        await asyncio.gather(*tasks)


asyncio.run(main())
