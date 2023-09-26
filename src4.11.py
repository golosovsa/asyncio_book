"""
Обработка исключений при использовании wait
с. 121
"""
import asyncio
import logging

from aiohttp import ClientSession
from util import async_timed
from chapter_04 import fetch_status


@async_timed()
async def main():
    async with ClientSession() as session:
        fetchers = [
            asyncio.create_task(fetch_status(session, 'https://example.com')),
            asyncio.create_task(fetch_status(session, 'python://bad')),
        ]

        done, pending = await asyncio.wait(fetchers)

        print(f'Число завершившихся задач {len(done)}')
        print(f'Число ожидающих задач {len(pending)}')

        for done_task in done:
            if done_task.exception() is None:
                print(done_task.result())
            else:
                logging.error('При выполнении запроса возникло исключение', exc_info=done_task.exception())


asyncio.run(main())
