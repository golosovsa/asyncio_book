"""
Обработка ошибки в транзакции
с. 147
"""
import asyncio
import logging

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

    try:
        async with connection.transaction():
            insert_brand = "INSERT INTO brand VALUES(9999, 'big_brand')"
            await connection.execute(insert_brand)
            await connection.execute(insert_brand)
    except Exception:
        logging.exception('Ошибка при выполнении транзакции')
    finally:
        query = "SELECT brand_name FROM brand WHERE brand_name like 'big_%'"
        brands = await connection.fetch(query)
        print(f'Результат запроса: {brands}')

    await connection.close()


asyncio.run(main())
