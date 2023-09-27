"""
Вставка случайных марок
с. 139
"""
import asyncpg
import asyncio
from random import sample

from util import get_secret


def load_common_words() -> list[str]:
    with open('common_words.txt', 'rt', encoding='utf-8') as common_words:
        return common_words.readlines()


def generate_brand_names(words: list[str]) -> list[tuple[str, ...]]:
    return [(words[index],) for index in sample(range(100), 100)]


async def insert_brands(common_words, connection) -> int:
    brands = generate_brand_names(common_words)
    insert_brands_query = 'INSERT INTO brand VALUES(DEFAULT, $1)'
    return await connection.executemany(insert_brands_query, brands)


async def main():
    common_words = load_common_words()
    connection = await asyncpg.connect(
        host='127.0.0.1',
        port=5432,
        user='postgres',
        database='products',
        password=get_secret('POSTGRES_PASSWORD'),
    )
    await insert_brands(common_words, connection)
    await connection.close()


asyncio.run(main())
