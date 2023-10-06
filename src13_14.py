"""
Разделение чтения вывода и записи ввода
с. 362
"""
import asyncio
from asyncio import StreamWriter, StreamReader, Event
from asyncio.subprocess import Process


async def output_consumer(input_ready_event: Event, stdout: StreamReader):
    while (data := await stdout.read(2048)) != b'':
        print(data.decode())
        if data.decode().endswith('Введите текст: '):
            input_ready_event.set()


async def input_writer(text_data, input_ready_event: Event, stdin: StreamWriter):
    for text in text_data:
        await input_ready_event.wait()
        stdin.write(text.encode())
        await stdin.drain()
        input_ready_event.clear()


async def main():
    program = ['python', 'src13_13.py']
    process: Process = await asyncio.create_subprocess_exec(
        *program,
        stdout=asyncio.subprocess.PIPE,
        stdin=asyncio.subprocess.PIPE,
    )

    input_ready_event = asyncio.Event()

    text_input = ['one\n', 'two\n', 'three\n', 'four\n', 'quit\n']

    await asyncio.gather(
        output_consumer(input_ready_event, process.stdout),
        input_writer(text_input, input_ready_event, process.stdin),
        process.wait(),
    )


asyncio.run(main())
