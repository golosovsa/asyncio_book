"""
Многопоточный эхо-сервер
с. 191
"""
from threading import Thread
import socket


def echo(client: socket):
    while True:
        data = client.recv(2048)
        print(f'Получено {data}, отправляем!')
        client.sendall(data)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('127.0.0.1', 8000))
    server.listen()
    while True:
        connection, _ = server.accept()
        thread = Thread(target=echo, args=(connection, ))
        thread.start()
