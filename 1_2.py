# 2. Каждое из слов «class», «function», «method» записать в байтовом типе. Сделать это необходимо в автоматическом,
# а не ручном режиме, с помощью добавления литеры b к текстовому значению, (т.е. ни в коем случае не используя
# методы encode, decode или функцию bytes) и определить тип, содержимое и длину соответствующих переменных.

my_list = ['class', 'function', 'method']


def str_to_bytes(str_word):
    # byte_word = eval("b'{}'".format(str_word))
    byte_word = eval(f"b'{str_word}'")
    return type(byte_word), byte_word, len(byte_word)


for i in range(0, len(my_list)):
    print(str_to_bytes(my_list[i]))
