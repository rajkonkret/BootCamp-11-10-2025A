import asyncio
import time
import aiohttp


async def fetch(url, session, index):
    async with session.get(url, ssl=False) as response:
        text = await response.text()
        print(f"Text: {text}")

        return response.status
