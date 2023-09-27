"""
Использование сопрограммы execute для выполнения команд create
с. 136
"""
import asyncio

import asyncpg

from src5_2 import CREATE_BRAND_TABLE, CREATE_PRODUCT_TABLE, CREATE_PRODUCT_COLOR_TABLE, CREATE_PRODUCT_SIZE_TABLE, \
    CREATE_SKU_TABLE, SIZE_INSERT, COLOR_INSERT
from util import get_secret


async def main():
    connection = await asyncpg.connect(
        host='127.0.0.1',
        port=5432,
        user='postgres',
        database='products',
        password=get_secret('POSTGRES_PASSWORD'),
    )
    statements = [
        CREATE_BRAND_TABLE,
        CREATE_PRODUCT_TABLE,
        CREATE_PRODUCT_COLOR_TABLE,
        CREATE_PRODUCT_SIZE_TABLE,
        CREATE_SKU_TABLE,
        SIZE_INSERT,
        COLOR_INSERT,
    ]
    print('Создается база данных product...')
    for statement in statements:
        status = await connection.execute(statement)
        print(status)
    print('База данных product создана!')
    await connection.close()


asyncio.run(main())
