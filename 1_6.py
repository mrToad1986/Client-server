# 6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет»,
# «декоратор». Далее забыть о том, что мы сами только что создали этот файл и исходить из того,
# что перед нами файл в неизвестной кодировке. Задача: открыть этот файл БЕЗ ОШИБОК вне зависимости от того,
# в какой кодировке он был создан.

from chardet import detect

lines = [
    'сетевое программирование',
    'сокет',
    'декоратор'
]
file = open('test_file.txt', 'w', encoding='utf-8')
for line in lines:
    file.write(line)
    file.write('\n')
file.close()

with open('test_file.txt', 'rb') as file:
    content = file.read()
encoding = detect(content)['encoding']
print('file encoding: ', encoding)

with open('test_file.txt', encoding=encoding) as file_open:
    for line in file_open:
        print(line)
