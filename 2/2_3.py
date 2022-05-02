# 3. Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение данных
# в файле YAML-формата. Для этого:
# Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список,
# второму — целое число, третьему — вложенный словарь,
# где значение каждого ключа — это целое число с юникод-символом, отсутствующим в кодировке ASCII (например, €);
# Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml.
# При этом обеспечить стилизацию файла с помощью параметра default_flow_style,
# а также установить возможность работы с юникодом: allow_unicode = True;
# Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.

import yaml
from pprint import pprint

currency_portfolio = {
    'currency': ['USD', 'EUR', 'GBP', 'JPY', 'BTC'],
    'positions': 5,
    'volume': {
        'US Dollar': '5000\u0024',
        'Euro': '10000\u20ac',
        'GB Pound': '5000\u00a3',
        'Japanese Yena': '1000000\u00a5',
        'Bitcoin': '1.2611\u20bf',
    }
}

with open('currency.yaml', 'w', encoding='utf-8') as input_object:
    yaml.dump(currency_portfolio, input_object, default_flow_style=False, allow_unicode=True, sort_keys=False)

with open('currency.yaml', 'r', encoding='utf-8') as output_object:
    output = yaml.load(output_object, Loader=yaml.SafeLoader)
    pprint(output)

if currency_portfolio == output:
    print("Чтение произведено верно")
else:
    print("Ошибка чтения файла")
