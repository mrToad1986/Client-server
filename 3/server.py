# Серверная часть
# Функции сервера:
# принимает сообщение клиента;
# формирует ответ клиенту;
# отправляет ответ клиенту;
# имеет параметры командной строки:
# -p <port> — TCP-порт для работы (по умолчанию использует 7777)
# -a <addr> — IP-адрес для прослушивания (по умолчанию слушает все доступные адреса - " ")

import json
import socket
import argparse
import logging
from sys import argv, exit
from logs import server_log_config
from common.utils import get_message, send_message
from common.variables import DEFAULT_PORT, MAX_CONNECTIONS, ACTION, TIME, USER, ACCOUNT_NAME, PRESENCE, RESPONSE, ERROR
from decorators import log

# Создание именованного логгера для сервера
server_logger = logging.getLogger('server_log')


# проверка сообщений от клиента

@log
def process_client_message(message):
    server_logger.debug(f'Получен ответ от клиента: {message}')
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message and USER in message \
            and message[USER][ACCOUNT_NAME] == 'Guest':
        return {RESPONSE: 200}
    return {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }


def main():
    # получение параметров при запуске из коммандной строки с помощью argparse
    parser = argparse.ArgumentParser(description='port, ip_address')
    parser.add_argument('-p', '--port', type=int, default=DEFAULT_PORT)
    parser.add_argument('-a', '--address', type=str, default='')
    args = parser.parse_args()

    # получение номера порта
    try:
        listen_port = args.port
        # print(listen_port)
        server_logger.info(f'Получен номер порта для подключения к серверу: {listen_port}')
        if not isinstance(listen_port, int):
            raise TypeError
        if listen_port not in range(1024, 65536):
            raise ValueError
    except TypeError:
        # print('Неверный формат значения номера порта')
        server_logger.critical(f'Неверный формат значения номера порта: {listen_port}')
        exit(1)
    except ValueError:
        # print('Номер порта должен быть в диапазоне от 1024 до 65535')
        server_logger.error(f'Номер порта {listen_port} должен быть в диапазоне от 1024 до 65535')
        exit(1)
    # получение ip-адреса
    try:
        listen_address = args.address
        # print(listen_address)
        server_logger.info(f'Получен IP-адрес для подключения к серверу: {listen_address}')
    except:
        # print('Неверно указан ip-адрес')
        server_logger.error(f'Получено неверное значение IP-адреса: {listen_address}')

    # Инициализация сокета и обмен данными
    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    transport.bind((listen_address, listen_port))
    transport.listen(MAX_CONNECTIONS)

    while True:
        client, client_address = transport.accept()
        try:
            message_from_client = get_message(client)
            # print(message_from_client)
            server_logger.debug((f'Получено сообщение от клиента: {message_from_client}'))
            response = process_client_message(message_from_client)
            server_logger.debug(f'Сформирован ответ клиенту: {response}')
            send_message(client, response)
            server_logger.debug(f'Соединение с клиентом закрывается')
            client.close()
        except (ValueError, json.JSONDecodeError):
            # print('Принято некорректное сообщение от клиента.')
            server_logger.error(f'Принято некорректное сообщение от клиента. '
                                f'Соединение с клиентом закрывается')
            client.close()


if __name__ == '__main__':
    main()
