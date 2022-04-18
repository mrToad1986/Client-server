# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового
# в строковый тип на кириллице.

import subprocess
import platform
import chardet

if platform.system().lower() == 'windows':
    param = '-n'
else:
    param = '-c'
args = [
    ['ping', param, '3', 'yandex.ru'],
    ['ping', param, '3', 'youtube.com'],
    ['ping', param, '3', 'dw.de']  # заблокированный в РФ ресурс добавлен ради интереса
]

for i in range(0, len(args)):
    process = subprocess.Popen(args[i], stdout=subprocess.PIPE)
    for line in process.stdout:
        result = chardet.detect(line)
        print('result = ', result)
        line = line.decode(result['encoding']).encode('utf-8')
        print(line.decode('utf-8'))
