"""
Хронометраж двух конкурентных задач с помощью декоратора
с. 64
"""
import asyncio

from util import async_timed


@async_timed()
async def delay(delay_seconds: int) -> int:
    print(f'Засыпаю на {delay_seconds} секунд')
    await asyncio.sleep(delay_seconds)
    print(f'Сон в течение {delay_seconds} секунд закончился')
    return delay_seconds


@async_timed()
async def main():
    task_one = asyncio.create_task(delay(2))
    task_two = asyncio.create_task(delay(3))

    await task_one
    await task_two


asyncio.run(main())
