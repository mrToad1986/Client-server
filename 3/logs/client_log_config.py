import os
import sys
import logging
import logging.handlers

client_formatter = logging.Formatter('%(asctime)-26s %(levelname)-10s %(filename)s %(message)s')
'''
где:
%(asctime)s - Время, когда была выполнена запись в журнал, в формате ASCII
%(levelname)s - Символическое имя уровня важности (DEBUG, INFO и т.д.)
%(filename)s - Имя исходного файла, откуда была выполнена запись в журнал
%(message)s - Текст журналируемого сообщения (определяется пользователем)
'''

sys.path.append('../')
path = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(path, 'client_log.log')

stream_handler = logging.StreamHandler(sys.stderr)
stream_handler.setFormatter(client_formatter)
stream_handler.setLevel(logging.DEBUG)
log_file = logging.handlers.TimedRotatingFileHandler(path, encoding='utf-8')
log_file.setFormatter(client_formatter)

logger = logging.getLogger('client_log')
logger.addHandler(stream_handler)
logger.addHandler(log_file)
logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    logger.debug('отладочная информация')
    logger.info('отладочное сообщение')
    logger.warning('предупреждение')
    logger.error('ошибка')
    logger.critical('критическая ошибка')
