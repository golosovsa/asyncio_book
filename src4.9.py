"""
Задание тайм-аута для as_completed
с. 117
"""

import asyncio
from aiohttp import ClientSession

from chapter_04 import fetch_status
from util import async_timed


@async_timed()
async def main():
    async with ClientSession() as session:
        fetchers = [
            fetch_status(session, 'https://www.example.com', 0),
            fetch_status(session, 'https://www.example.com', 10),
            fetch_status(session, 'https://www.example.com', 10),
        ]

        for done_task in asyncio.as_completed(fetchers, timeout=2):
            try:
                result = await done_task
                print(result)
            except TimeoutError:
                print('Произошел тайм-аут!')

        for task in asyncio.all_tasks():
            print(task)

asyncio.run(main())
