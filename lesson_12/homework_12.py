import json
import csv
import openpyxl
import xlsxwriter


# Задание 1
def decode_encode():
    a = b'r\xc3\xa9sum\xc3\xa9'.decode('utf-8')
    print(a)

    a = a.encode('latin1')
    print(a)

    a = a.decode('latin1')
    print(a)


# Задание 2
def write_strings_in_txt():
    a = input('Введите первую строку: ')
    b = input('Введите вторую строку: ')
    c = input('Введите третью строку: ')
    d = input('Введите четвёртую строку: ')

    with open('four_lines.txt', 'w') as f:
        f.write(f'{a} \n{b}')

    with open('four_lines.txt', 'a') as f:
        f.write(f'\n{c} \n{d}')


# Задание 3
def save_dict_in_json():
    person_info = {'111111': ('Sam', 23),
                   '222222': ('Alex', 20),
                   '333333': ('Mike', 30),
                   '444444': ('Nancy', 26),
                   '555555': ('Stacey', 19)}

    with open('person_info.json', 'w') as f:
        json.dump(person_info, f, indent=4)


# Задание 4
def load_json_save_csv():
    phone_by_id = {'111111': '234-34-23',
                   '222222': '211-00-67',
                   '333333': '240-10-10',
                   '444444': '278-09-65',
                   '555555': '205-17-17'}

    with open('person_info.json') as f:
        data = json.load(f)

    with open('person_info_2.csv', 'w', newline='') as w_file:
        data_csv = csv.writer(w_file, delimiter=",")
        data_csv.writerow(['id', 'name', 'age', 'phone'])

        for key, value in data.items():
            data_csv.writerow([key, value[0], value[1], phone_by_id.get(key)])


# Задание 5
def load_csv_save_xlsx():
    with open('person_info_2.csv') as r_file:
        csv_reader = csv.reader(r_file, delimiter=',')
        csv_data = {rows[0]: [rows[1], rows[3]] for rows in csv_reader}

    workbook = xlsxwriter.Workbook('person_info_3.xlsx')
    worksheet = workbook.add_worksheet()
    count = 0

    for person in csv_data:
        if count != 0:
            worksheet.write(0, count, f'Person {count}')
        worksheet.write(1, count, person)
        worksheet.write(2, count, csv_data.get(person)[0])
        worksheet.write(3, count, csv_data.get(person)[1])
        count += 1

    workbook.close()


if __name__ == '__main__':
    load_csv_save_xlsx()
