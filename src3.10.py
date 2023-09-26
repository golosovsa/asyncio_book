"""
 Корректная остановка
 с. 97
"""
import asyncio
from asyncio import AbstractEventLoop
import socket as s
from socket import socket
import logging
import signal


async def echo(connection: socket, loop: AbstractEventLoop) -> None:
    try:
        while data := await loop.sock_recv(connection, 1024):
            print(f'Получены данные!')
            if data == b'boom\r\n':
                raise Exception('Неожиданная ошибка сети')
            await loop.sock_sendall(connection, data)

    except Exception as ex:
        logging.exception(ex)
    finally:
        connection.close()


echo_tasks = []


async def connection_listener(server_socket: socket, loop: AbstractEventLoop):
    while True:
        connection, address = await loop.sock_accept(server_socket)
        connection.setblocking(False)
        print(f'Получен запрос на подключение от {address}')
        echo_task = asyncio.create_task(echo(connection, loop))
        echo_tasks.append(echo_task)


class GracefulExit(SystemExit):
    pass


def shutdown():
    raise GracefulExit()


async def close_echo_tasks(opened_echo_tasks: list[asyncio.Task]):
    waiters = [asyncio.wait_for(task, 2) for task in opened_echo_tasks]
    for task in waiters:
        try:
            await task
        except asyncio.TimeoutError:
            pass


async def main():
    server_socket = socket()
    server_socket.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)

    server_address = ('127.0.0.1', 8000)
    server_socket.setblocking(False)
    server_socket.bind(server_address)
    server_socket.listen()

    for signame in {'SIGINT', 'SIGTERM'}:
        loop.add_signal_handler(getattr(signal, signame), shutdown)
    await connection_listener(server_socket, loop)


loop = asyncio.new_event_loop()

try:
    loop.run_until_complete(main())
except GracefulExit:
    loop.run_until_complete(close_echo_tasks(echo_tasks))
finally:
    loop.close()