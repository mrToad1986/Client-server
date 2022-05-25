import os
import sys
import logging
import logging.handlers

server_formatter = logging.Formatter('%(asctime)-26s %(levelname)-10s %(filename)-16s %(funcName)-12s %(message)s')
'''
где:
%(asctime)s - Время, когда была выполнена запись в журнал, в формате ASCII
%(levelname)s - Символическое имя уровня важности (DEBUG, INFO и т.д.)
%(filename)s - Имя исходного файла, откуда была выполнена запись в журнал
%(message)s - Текст журналируемого сообщения (определяется пользователем)
%(funcName)s - Имя функции, выполнившей запись в журнал
'''

sys.path.append('../')
path = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(path, 'server_log.log')

stream_handler = logging.StreamHandler(sys.stderr)
stream_handler.setFormatter(server_formatter)
stream_handler.setLevel(logging.DEBUG)
log_file = logging.handlers.TimedRotatingFileHandler(path, encoding='utf-8', interval=1, when='midnight', utc=False)
log_file.setFormatter(server_formatter)

logger = logging.getLogger('server_log')
logger.addHandler(stream_handler)
logger.addHandler(log_file)
logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    logger.debug('отладочная информация')
    logger.info('отладочное сообщение')
    logger.warning('предупреждение')
    logger.error('ошибка')
    logger.critical('критическая ошибка')
