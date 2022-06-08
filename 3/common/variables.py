# Системные переменные

#сетевые подключения
DEFAULT_PORT = 7777
DEFAULT_IP_ADDR = '127.0.0.1'
MAX_CONNECTIONS = 10 # число пользователей в очереди
MAX_MSG_LENGTH = 2048
ENCODING = 'utf-8'

#протокол JIM (JSON Instant messaging)
ACTION = 'action'
TIME = 'time'
USER = 'user'
ACCOUNT_NAME = 'account_name'
SENDER = 'from'
DESTINATION = 'to'

#прочее
PRESENCE = 'presence'
RESPONSE = 'response'
ERROR = 'error'
MESSAGE = 'message'
MESSAGE_TEXT = 'mess_text'
EXIT = 'exit'

#ответы
RESPONSE_200 = {RESPONSE: 200}
RESPONSE_400 = {
    RESPONSE: 400,
    ERROR: None
}
