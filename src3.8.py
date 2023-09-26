"""
Построение асинхронного эхо-сервера + обработка ошибок при отказе задач
с. 91
"""
import asyncio
import logging
import socket as s
from socket import socket
from asyncio import AbstractEventLoop


async def echo(connection: socket, loop:AbstractEventLoop) -> None:
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


async def listen_for_connection(server_socket: socket, loop: AbstractEventLoop):
    while True:
        connection, address = await loop.sock_accept(server_socket)
        connection.setblocking(False)
        print(f'Получен запрос на подключение от {address}')
        asyncio.create_task(echo(connection, loop))


async def main():
    server_socket = socket(s.AF_INET, s.SOCK_STREAM)
    server_socket.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)

    server_address = ('127.0.0.1', 8000)
    server_socket.setblocking(False)
    server_socket.bind(server_address)
    server_socket.listen()

    await listen_for_connection(server_socket, asyncio.get_event_loop())


asyncio.run(main())
