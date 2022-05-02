# 1. Задание на закрепление знаний по модулю CSV.
# Написать скрипт, осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt, info_3.txt
# и формирующий новый «отчетный» файл в формате CSV. Для этого:
# Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие
# и считывание данных. В этой функции из считанных данных необходимо с помощью регулярных выражений
# извлечь значения параметров «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
# Значения каждого параметра поместить в соответствующий список. Должно получиться четыре списка — например,
# os_prod_list, os_name_list, os_code_list, os_type_list. В этой же функции создать главный список для
# хранения данных отчета — например, main_data — и поместить в него названия столбцов отчета в виде списка:
# «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения для этих столбцов также оформить
# в виде списка и поместить в файл main_data (также для каждого файла);
# Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
# В этой функции реализовать получение данных через вызов функции get_data(),
# а также сохранение подготовленных данных в соответствующий CSV-файл;
# Проверить работу программы через вызов функции write_to_csv().

import os
import re
import csv
from chardet import detect

os_prod_list = []
os_name_list = []
os_code_list = []
os_type_list = []
main_data = []


def get_data():
    for filename in os.scandir():
        if re.fullmatch(r'\S+.txt', filename.name):
            with open(filename, 'rb') as io_object:
                byte_content = io_object.read()
                encoding = detect(byte_content)['encoding']
                content = byte_content.decode(encoding)

            re_prod = re.compile(r'Изготовитель системы:\s*\S*')
            os_prod_list.append(re_prod.findall(content)[0].split()[2])

            re_name = re.compile(r'Название ОС:\s*\S*\s+\S*\s+\w*\s+\S*')
            os_name_list.append(' '.join(re_name.findall(content)[0].split()[2:]))

            re_code = re.compile(r'Код продукта:\s*\S*')
            os_code_list.append(re_code.findall(content)[0].split()[2])

            re_type = re.compile(r'Тип системы:\s*\S*')
            os_type_list.append(re_type.findall(content)[0].split()[2])

    headers = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    raw_rows = [os_prod_list, os_name_list, os_code_list, os_type_list]
    main_data.append(headers)
    for row in range(0, len(raw_rows[0])):
        line = list(map(lambda formatted_row: formatted_row[row], raw_rows))
        main_data.append(line)

    return main_data


def write_to_csv(file_name):
    main_data = get_data()
    with open(file_name, 'w', encoding='utf-8', newline='') as f_n:
        # для MS Exсel указать кодировку 'windows-1251'
        # newline = '' для Windows - пропуск пустых строк при записи
        f_n_writer = csv.writer(f_n)
        for row in main_data:
            f_n_writer.writerow(row)


with open('output.csv', 'r', encoding='utf-8') as f_n:
    f_n_reader = csv.DictReader(f_n)
    for row in f_n_reader:
        print(row)