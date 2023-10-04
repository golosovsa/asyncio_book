"""
Сопрограмма retry
с. 294
"""
import asyncio
import logging
from typing import Callable, Awaitable


class TooManyRetries(Exception):
    """ Too many retries """


async def retry(coro: Callable[[], Awaitable], max_retries: int, timeout: float, retry_interval: float):
    for retry_num in range(0, max_retries):
        try:
            return await asyncio.wait_for(coro(), timeout=timeout)
        except Exception as e:
            logging.exception(
                f'Во время ожидания произошло исключение (попытка {retry_num}), пробую еще раз.',
                exc_info=e
            )
        await asyncio.sleep(retry_interval)
    raise TooManyRetries()
