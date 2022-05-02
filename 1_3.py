# 3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
# Важно: решение должно быть универсальным, т.е. не зависеть от того, какие конкретно слова мы исследуем.

my_list = ['attribute', 'класс', 'функция', 'type']


def is_ascii(word):
    ascii_list = [int(ord(cher)) for cher in word]
    # for i in range(0, len(word)):
    #     ascii_list.append(ord(word[i]))
    if max(ascii_list) > 127:
        return f'String "{word}" contains non-ASCII symbols and could not be converted to bytes'
    else:
        return f'String "{word}" is easily converted to bytes'


for i in range(0, len(my_list)):
    print(is_ascii(my_list[i]))
