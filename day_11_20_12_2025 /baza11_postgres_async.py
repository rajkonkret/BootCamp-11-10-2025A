import asyncio
import asyncpg
import psycopg2
# pip install asyncpg

async def run():
    conn = await asyncpg.connect(
        host="localhost",
        port=5432,
        database="mydatabase",
        user="myuser",
        password="mypassword"
    )

    await conn.fetch("CREATE TABLE IF NOT EXISTS persons(id SERIAL PRIMARY KEY, name TEXT);")
    await conn.close()


if __name__ == '__main__':
    asyncio.run(run())