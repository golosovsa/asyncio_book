"""
Взаимоблокировка при использовании канала
с. 355
"""
import asyncio
from asyncio.subprocess import Process


async def main():
    program = ['python', 'src13_4.py']
    process: Process = await asyncio.create_subprocess_exec(*program, stdout=asyncio.subprocess.PIPE)

    print(f'pid процесса: {process.pid}')

    return_code = await process.wait()
    print(f'Процесс вернул: {return_code}')


asyncio.run(main())
