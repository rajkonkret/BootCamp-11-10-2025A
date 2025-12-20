import asyncio
import asyncpg
import psycopg2
# pip install asyncpg

async def run():
    # conn = await asyncpg.connect(
    #     host="localhost",
    #     port=5432,
    #     database="mydatabase",
    #     user="myuser",
    #     password="mypassword"
    # )

    conn = await asyncpg.connect(
        host="",
        port=5432,
        database="",
        user="",
        password="",
        # ssl=True # jeśli serwer wymaga włacz to
    )


# domyślnie ma tryb auto-commit
    await conn.fetch("CREATE TABLE IF NOT EXISTS persons(id SERIAL PRIMARY KEY, name TEXT);")

    await conn.execute("""
    INSERT INTO persons (name) VALUES ($1);
    """, "Radek")

    await conn.close()


if __name__ == '__main__':
    asyncio.run(run())