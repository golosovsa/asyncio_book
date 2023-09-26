"""
Отмена медленного запроса
(работать не будет, тк после wait api_a и api_b будут обернуты в класс Task
и конструкция if task is api_b: не сработает
с. 128
"""
import asyncio

from aiohttp import ClientSession
from util import async_timed
from chapter_04 import fetch_status


@async_timed()
async def main():
    async with ClientSession() as session:
        api_a = fetch_status(session, 'https://example.com')
        api_b = fetch_status(session, 'https://example.com', delay=2)

        done, pending = await asyncio.wait([api_a, api_b], timeout=1)

        print(f'Число завершившихся задач {len(done)}')
        print(f'Число ожидающих задач {len(pending)}')

        for task in pending:
            if task is api_b:
                print('API B слишком медленный, отмена')
                task.cancel()


asyncio.run(main())
