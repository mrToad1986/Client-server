# 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления
# в байтовое и выполнить обратное преобразование (используя методы encode и decode).

my_list = ['разработка', 'администрирование', 'protocol', 'standard']

for i in range(0, len(my_list)):
    try:
        word = my_list[i]
        str_to_bytes = str.encode(word, 'utf-8')
        bytes_to_str = bytes.decode(str_to_bytes, 'utf-8')
        # тот же результат:
        # word = my_list[i]
        # str_to_bytes = word.encode('utf-8')
        # bytes_to_str = str_to_bytes.decode('utf-8')
        print(f'Converting string "{word}" to bytes:\n{str_to_bytes}\nand back to string:\n{bytes_to_str}\n')
    except:
        print(f'{word} is not a string')
