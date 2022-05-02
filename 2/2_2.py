# 2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
# Написать скрипт, автоматизирующий его заполнение данными. Для этого:
# Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
# цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря
# в файл orders.json. При записи данных указать величину отступа в 4 пробельных символа;
# Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.

import json
from pprint import pprint


def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json', 'r', encoding='utf-8') as output_object:
        my_data = json.load(output_object)
    with open('orders.json', 'w', encoding='utf-8') as input_object:
        orders_list = my_data['orders']
        order_info = {'item': item,
                      'quantity': quantity,
                      'price': price,
                      'buyer': buyer,
                      'date': date}
        orders_list.append(order_info)
        json.dump(my_data, input_object, indent=4, ensure_ascii=False)


write_order_to_json('GeForce RTX 3080', '4', '179000', 'Абрамов П.В.', '25.04.2022')
write_order_to_json('Lenovo Tab P11', '12', '32600', 'Петров В.А.', '27.04.2022')

# with open('orders.json', encoding='utf-8') as io_object:
#     result = json.load(io_object)
#     pprint(result)
#     # content = io_object.read()
#     # result = json.loads(content)
#     # for key, value in result.items():
#     #     print (key, ' ', value)