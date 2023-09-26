"""
Обработка всех результатов по мере поступления
с. 125
"""
import asyncio

from aiohttp import ClientSession
from util import async_timed
from chapter_04 import fetch_status


@async_timed()
async def main():
    async with ClientSession() as session:
        url = 'https://example.com'
        pending = [
            asyncio.create_task(fetch_status(session, url)),
            asyncio.create_task(fetch_status(session, url)),
            asyncio.create_task(fetch_status(session, url)),
        ]

        while pending:
            done, pending = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED)

            print(f'Число завершившихся задач {len(done)}')
            print(f'Число ожидающих задач {len(pending)}')

            for done_task in done:
                print(await done_task)

asyncio.run(main())
