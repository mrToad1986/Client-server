# Клиентская часть
# Функции клиента:
# сформировать presence-сообщение;
# отправить сообщение серверу;
# получить ответ сервера;
# разобрать сообщение сервера;
# параметры командной строки скрипта client.py <addr> [<port>]:
# addr — ip-адрес сервера, по умолчанию 127.0.0.1;
# port — tcp-порт на сервере, по умолчанию 7777.

import json
import socket
import time
import sys
import logging
from logs import client_log_config
from common.utils import get_message, send_message
from common.variables import DEFAULT_PORT, DEFAULT_IP_ADDR, ACTION, TIME, USER, ACCOUNT_NAME, PRESENCE, RESPONSE, ERROR

# Создание именованного логгера для сервера
client_logger = logging.getLogger('client_log')

# инициализация пользователя
def create_presence(account_name='Guest'):
    out = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    client_logger.debug(f'Создано сообщение {PRESENCE} для пользователя {account_name}')
    return out

# обработка ответа сервера
def process_ans(message):
    client_logger.debug(f'Получен ответ от сервера: {message}')
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            return '200 : OK'
        return f'400 : {message[ERROR]}'
    raise ValueError


def main():
    # получение параметров при запуске из коммандной строки с помощью sys.argv
    try:
        server_address = sys.argv[1]
        server_port = int(sys.argv[2])
        if server_port not in range(1024, 65536):
            raise ValueError
    except IndexError:
        server_address = DEFAULT_IP_ADDR
        server_port = DEFAULT_PORT
        client_logger.debug(f'Значение IP-адреса установлено по умолчанию: {DEFAULT_IP_ADDR}')
        client_logger.debug(f'Значение порта установлено по умолчанию: {DEFAULT_PORT}')
    except ValueError:
        # print('Номер порта должен быть в диапазоне от 1024 до 65535')
        client_logger.critical(f'Номер порта {server_port} должен быть в диапазоне от 1024 до 65535')
        sys.exit(1)
    # print(server_address)
    # print(server_port)
    client_logger.debug(f'Получен IP-адрес: {server_address}')
    client_logger.debug(f'Получен порт: {server_port}')

    # Инициализация сокета и обмен данными
    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.connect((server_address, server_port))
    message_to_server = create_presence()
    send_message(transport, message_to_server)
    try:
        answer = process_ans(get_message(transport))
        # print(answer)
        client_logger.debug(f'Получено сообщение от сервера: {answer}')
    except (ValueError, json.JSONDecodeError):
        # print('Некорректное сообщение от сервера')
        client_logger.error('Некорректное сообщение от сервера')

if __name__ == '__main__':
    main()