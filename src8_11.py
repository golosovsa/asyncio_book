"""
Асинхронный командный SQL клиент
с. 240
"""
import asyncio
import sys

import asyncpg
import os
import tty
from collections import deque
from asyncpg.pool import Pool
from src8_5 import create_stdin_reader
from src8_7 import save_cursor_position, restore_cursor_position, move_to_top_of_screen, move_to_bottom_of_screen, \
    delete_line
from src8_8 import read_line
from src8_9 import MessageStorage
from util import get_secret


async def run_query(query: str, pool: Pool, message_storage: MessageStorage):
    async with pool.acquire() as connection:
        try:
            result = await connection.fetchrow(query)
            await message_storage.append(f'Выбрано {len(result)} строк по запросу: {query}')
        except Exception as e:
            await message_storage.append(f'Получено исключение {e} от: {query}')


async def main():
    tty.setcbreak(sys.stdin)
    os.system('clear')
    rows = move_to_bottom_of_screen()

    async def redraw_output(items: deque):
        save_cursor_position()
        move_to_top_of_screen()
        for item in items:
            delete_line()
            print(item)
        restore_cursor_position()

    messages = MessageStorage(redraw_output, rows - 1)

    stdin_reader = await create_stdin_reader()

    async with asyncpg.create_pool(
        host='127.0.0.1',
        port=5432,
        user='postgres',
        database='products',
        password=get_secret('POSTGRES_PASSWORD'),
        min_size=6,
        max_size=6,
    ) as pool:
        while True:
            query = await read_line(stdin_reader)
            asyncio.create_task(run_query(query, pool, messages))


asyncio.run(main())
