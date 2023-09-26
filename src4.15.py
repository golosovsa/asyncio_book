"""
Использование тайм-аутов в wait
с. 127
"""
import asyncio

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
            asyncio.create_task(fetch_status(session, url, delay=3)),
        ]

        done, pending = await asyncio.wait(fetchers, timeout=1)

        print(f'Число завершившихся задач {len(done)}')
        print(f'Число ожидающих задач {len(pending)}')

        for done_task in done:
            print(await done_task)

asyncio.run(main())
