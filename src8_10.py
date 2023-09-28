"""
Приложение для асинхронной задержки
с. 239
"""
import asyncio
import os
import sys
import tty
from collections import deque
from src8_5 import create_stdin_reader
from src8_7 import (
    save_cursor_position,
    restore_cursor_position,
    move_to_top_of_screen,
    delete_line,
    move_to_bottom_of_screen,
)
from src8_8 import read_line
from src8_9 import MessageStorage


async def sleep(delay: int, message_store: MessageStorage):
    await message_store.append(f'Начало задержки {delay}')
    await asyncio.sleep(delay)
    await message_store.append(f'Конец задержки {delay}')


async def main():
    tty.setcbreak(sys.stdin)
    os.system('clear')
    rows = move_to_bottom_of_screen()

    async def redraw_output(items: deque):
        save_cursor_position()
        move_to_top_of_screen()
        for item in items:
            delete_line()
            print(item)
        restore_cursor_position()

    messages = MessageStorage(redraw_output, rows - 1)

    stdin_reader = await create_stdin_reader()

    while True:
        line = await read_line(stdin_reader)
        delay_time = int(line)
        asyncio.create_task(sleep(delay_time, messages))


asyncio.run(main())
