"""
Обработка запросов по мере завершения
с. 124
"""
import asyncio
import logging

from aiohttp import ClientSession
from util import async_timed
from chapter_04 import fetch_status


@async_timed()
async def main():
    async with ClientSession() as session:
        url = 'https://example.com'
        fetchers = [
            asyncio.create_task(fetch_status(session, url)),
            asyncio.create_task(fetch_status(session, url)),
            asyncio.create_task(fetch_status(session, url)),
        ]

        done, pending = await asyncio.wait(fetchers, return_when=asyncio.FIRST_COMPLETED)

        print(f'Число завершившихся задач {len(done)}')
        print(f'Число ожидающих задач {len(pending)}')

        for done_task in done:
            print(await done_task)

asyncio.run(main())
