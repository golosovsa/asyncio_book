"""
Использование communicate со стандартным вводом
с. 360
"""
import asyncio
from asyncio.subprocess import Process


async def main():
    program = ['python', 'src13_9.py']
    process: Process = await asyncio.create_subprocess_exec(
        *program,
        stdout=asyncio.subprocess.PIPE,
        stdin=asyncio.subprocess.PIPE,
    )

    stdout, stderr = await process.communicate(b'Zoot')
    print(stdout.decode())
    print(stderr)


asyncio.run(main())
