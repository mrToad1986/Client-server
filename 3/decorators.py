'''
1. Реализовать декоратор @log, фиксирующий обращение к декорируемой функции. Он сохраняет ее имя и аргументы.
2. В декораторе @log реализовать фиксацию функции, из которой была вызвана декорированная.
В логе должна быть отражена информация:
"<дата-время> Функция func_z() вызвана из функции main"
'''

import sys
import logging
import logs.server_log_config
import logs.client_log_config
import traceback
from datetime import datetime


def log(logging_func):
    def log_saver(*args, **kwargs):
        if 'server.py' in sys.argv[0]:
            logger_name = 'server_log'
        else:
            logger_name = 'client_log'
        logger = logging.getLogger(logger_name)
        res = logging_func(*args, **kwargs)
        logger.info(
            f'<{datetime.now()}> Функция {logging_func.__name__} с аргументами вызвана '
            f'из функции {traceback.format_stack()[0].strip().split()[-1]}'
        )
        logger.debug(
            f'<{datetime.now()}> Функция {logging_func.__name__} с аргументами вызвана '
            f'из функции {traceback.format_stack()[0].strip().split()[-1]}'
        )
        logger.error(
            f'<{datetime.now()}> Функция {logging_func.__name__} с аргументами вызвана '
            f'из функции {traceback.format_stack()[0].strip().split()[-1]}'
        )
        '''
        Насчет значения <дата-время> в формате записываемого в лог сообщения я наверное понял ТЗ
        слишком буквально, эти данные и так есть в логе,
        но с вашего позволения оставлю как есть.
        '''
        return res

    return log_saver
