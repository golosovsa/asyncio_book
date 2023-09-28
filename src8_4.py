"""
Попытка выполнения задач в фоновом режиме
с. 231
"""
import asyncio
from util import delay


async def main():
    while True:
        delay_time = input('Введите имя сна: ')
        asyncio.create_task(delay(int(delay_time)))


asyncio.run(main())
