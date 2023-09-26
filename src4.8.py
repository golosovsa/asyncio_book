"""
Использование as_completed
с. 116
"""
import asyncio
from aiohttp import ClientSession

from chapter_04 import fetch_status
from util import async_timed


@async_timed()
async def main():
    async with ClientSession() as session:
        fetchers = [
            fetch_status(session, 'https://www.example.com', 1),
            fetch_status(session, 'https://www.example.com', 1),
            fetch_status(session, 'https://www.example.com', 10),
        ]

        for finished_task in asyncio.as_completed(fetchers):
            print(await finished_task)


asyncio.run(main())
