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
import select
import time
from sys import argv, exit
from logs import server_log_config
from common.utils import get_message, send_message
from common.variables import DEFAULT_PORT, MAX_CONNECTIONS, ACTION, TIME, USER, ACCOUNT_NAME, PRESENCE, RESPONSE, ERROR
from decorators import log

# Создание именованного логгера для сервера
server_logger = logging.getLogger('server_log')


# проверка сообщений от клиента

@log
def process_client_message(message, message_list, client):
    server_logger.debug(f'Получен ответ от клиента: {message}')
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message and USER in message \
            and message[USER][ACCOUNT_NAME] == 'Guest':
        send_message(client, {RESPONSE: 200})
        return
    elif ACTION in message and message[ACTION] == MESSAGE and \
            TIME in message and MESSAGE_TEXT in message:
        messages_list.append((message[ACCOUNT_NAME], message[MESSAGE_TEXT]))
        return
    else:
        send_message(client, {RESPONSE: 400, ERROR: 'Bad Request'})
    return


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

    clients = []
    messages = []

    while True:
        try:
            client, client_address = transport.accept()
        except OSError as err:
            print(err.errno)
            pass
        else:
            LOGGER.info(f'Установлено соедение с ПК {client_address}')
            clients.append(client)

        recv_data_lst = []
        send_data_lst = []
        err_lst = []

        try:
            if clients:
                recv_data_lst, send_data_lst, err_lst = select.select(clients, clients, [], 0)
        except OSError:
            pass

        if recv_data_lst:
            for client_with_message in recv_data_lst:
                try:
                    process_client_message(get_message(client_with_message),
                                           messages, client_with_message)
                except:
                    LOGGER.info(f'Клиент {client_with_message.getpeername()} '
                                f'отключился от сервера.')
                    clients.remove(client_with_message)

        if messages and send_data_lst:
            message = {
                ACTION: MESSAGE,
                SENDER: messages[0][0],
                TIME: time.time(),
                MESSAGE_TEXT: messages[0][1]
            }
            del messages[0]
            for waiting_client in send_data_lst:
                try:
                    send_message(waiting_client, message)
                except:
                    LOGGER.info(f'Клиент {waiting_client.getpeername()} отключился от сервера.')
                    waiting_client.close()
                    clients.remove(waiting_client)


if __name__ == '__main__':
    main()
