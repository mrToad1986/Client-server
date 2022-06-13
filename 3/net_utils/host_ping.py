# 1. Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться
# доступность сетевых узлов. Аргументом функции является список, в котором каждый сетевой узел
# должен быть представлен именем хоста или ip-адресом. В функции необходимо перебирать ip-адреса
# и проверять их доступность с выводом соответствующего сообщения («Узел доступен», «Узел недоступен»).
# При этом ip-адрес сетевого узла должен создаваться с помощью функции ip_address().
# (Внимание! Аргументом сабпроцеса должен быть список, а не строка!!! Для уменьшения времени работы
# скрипта при проверке нескольких ip-адресов, решение необходимо выполнить с помощью потоков)

import os
import threading
import subprocess
from pprint import pprint
from ipaddress import ip_address

result = {'Доступные узлы': "", 'Недоступные узлы': ""}

def check_is_ip(value):
    try:
        ipv4 = ip_address(value)
    except ValueError:
        raise Exception('Неверно указан ip-адрес')
    return ipv4

def ping (ipv4, result, get_list):
    if os.name == 'nt':
        param = '-n'
    else:
        param = '-c'
    response = subprocess.Popen(["ping", param, '1', '-w', '1', str(ipv4)], stdout=subprocess.PIPE)
    if response.wait() == 0:
        result["Доступные узлы"] += f"{ipv4}\n"
        res = f"{ipv4} - Узел доступен"
        if not get_list:
            print(res)
        return res
    else:
        result["Недоступные узлы"] += f"{ipv4}\n"
        res = f"{ipv4} - Узел недоступен"
        if not get_list:
            print(res)
        return res

def host_ping(hosts_list, get_list=False):
    threads = []
    for host in hosts_list:
        try:
            ipv4 = check_is_ip(host)
        except:
            ipv4 = host
        thread = threading.Thread(target=ping, args=(ipv4, result, get_list), daemon=True)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    if get_list:
        return result


if __name__ == '__main__':
    hosts_list = ['yandex.ru', 'google.com', 'dw.de', 'youtube.com',
                  'facebook.com', '176.119.159.87', '192.168.0.1', '10.38.54.1',
                  '127.0.0.1', '8.8.8.8', '198.18.0.0', '255.255.255.255']
    host_ping(hosts_list)
    pprint(result)