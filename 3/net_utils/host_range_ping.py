# 2. Написать функцию host_range_ping() (возможности которой основаны на функции из примера 1 для
# перебора ip-адресов из заданного диапазона. Меняться должен только последний октет каждого адреса.
# По результатам проверки должно выводиться соответствующее сообщение.

from host_ping import check_is_ip, host_ping


def host_range_ping(get_list=False):
    while True:
        start_ip = input("Введите ip-адрес: ")
        try:
            ipv4_start = check_is_ip(start_ip)
            last_oct = int(start_ip.split('.')[3])
            break
        except Exception as exception:
            print(exception)
    while True:
        end_ip = input("Сколько адресов проверить?: ")
        if not end_ip.isnumeric():
            print("Необходимо ввести количество проверяемых адресов")
        else:
            if (last_oct + int(end_ip)) > 255 + 1:
                print(f"Диапазон проверяемых адресов выходит за пределы последнего октета")
            else:
                break
    host_list = []
    [host_list.append(str(ipv4_start + x)) for x in range(int(end_ip))]
    if not get_list:
        host_ping(host_list)
    else:
        return host_ping(host_list, True)


if __name__ == "__main__":
    host_range_ping()
