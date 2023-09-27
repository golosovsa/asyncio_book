"""
Подключение к базе данных postgres от имени пользователя по умолчанию
с. 132
"""
import asyncpg
import asyncio

from util import get_secret


async def main():
    connection = await asyncpg.connect(
        host='127.0.0.1',
        port=5432,
        user='postgres',
        database='postgres',
        password=get_secret('POSTGRES_PASSWORD'),
    )
    version = connection.get_server_version()
    print(f'Подключено! Версия Postgres равна {version}')
    await connection.close()


asyncio.run(main())
