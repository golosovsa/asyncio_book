"""
Получение заданного числа элементов с помощью асинхронного генератора
"""
import asyncio
import asyncpg

from util import get_secret


async def take(generator, to_take: int):
    item_count = 0
    async for item in generator:
        if item_count > to_take - 1:
            return
        item_count += 1
        yield item


async def main():
    connection = await asyncpg.connect(
        host='127.0.0.1',
        port=5432,
        user='postgres',
        database='products',
        password=get_secret('POSTGRES_PASSWORD'),
    )

    async with connection.transaction():
        query = 'SELECT product_id, product_name FROM product'
        product_generator = connection.cursor(query)

        async for product in take(product_generator, 5):
            print(product)

        print('Получены первые 5 товаров!')

    await connection.close()


asyncio.run(main())
