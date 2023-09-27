"""
Потоковая обработка результатов
с. 153
"""
import asyncio
import asyncpg

from util import get_secret


async def main():
    connection = await asyncpg.connect(
        host='127.0.0.1',
        port=5432,
        user='postgres',
        database='products',
        password=get_secret('POSTGRES_PASSWORD'),
    )

    query = 'SELECT product_id, product_name FROM product'
    async with connection.transaction():
        async for product in connection.cursor(query):
            print(product)

    await connection.close()


asyncio.run(main())
