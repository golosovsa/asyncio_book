"""
Сопрограммы на основе генераторов
с. 373
"""
import asyncio


@asyncio.coroutine
def coroutine():
    print('Засыпаю!')
    yield from asyncio.sleep(1)
    print('Просыпаюсь!')


asyncio.run(coroutine())
