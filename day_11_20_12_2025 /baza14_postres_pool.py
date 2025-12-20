import asyncio
import asyncpg


async def main():
    pool = await asyncpg.create_pool(
        host="localhost",
        port=5432,
        database="mydatabase",
        user="myuser",
        password="mypassword"
    )

    async with pool.acquire() as conn:
        async with conn.transaction():
            await conn.execute(
                "CREATE TABLE IF NOT EXISTS friends(id SERIAL PRIMARY KEY, name TEXT);"
            )

            row = await conn.fetchrow(
                "INSERT INTO friends(name) VALUES($1) RETURNING id, name;", "John"
            )
            print(f"Inserted: {dict(row)}")

    await pool.close()


if __name__ == '__main__':
    asyncio.run(main())
