# Утилиты

import json
from common.variables import MAX_MSG_LENGTH, ENCODING

import sys
sys.path.append('../')
from decorators import log

#прием и декодирование (байты -> строка(loads) -> словарь) сообщения
@log
def get_message(client):
    encoded_response = client.recv(MAX_MSG_LENGTH)
    if isinstance(encoded_response, bytes):
        json_response = encoded_response.decode(ENCODING)
        if isinstance(json_response, str):
            response = json.loads(json_response)
            if isinstance(response, dict):
                return response
            raise ValueError
        raise ValueError
    raise ValueError

#кодирование (словарь -> строка(dumps) -> байты) и отправка сообщения
@log
def send_message(sock, message):
    if not isinstance(message, dict):
        raise TypeError
    json_message = json.dumps(message)
    encoded_message = json_message.encode(ENCODING)
    sock.send(encoded_message)
