import view as v
import csv
import os.path

def write_data():
    name = v.correct_name('\nВведите Имя : ')  # запрашиваем ввод у пользователя
    sec_name = v.any_name('Введите Отчество (если нет отчества "-"): ')
    surname = v.correct_name('Введите Фамилию : ')
    phone = v.correct_number()

    if os.path.exists('data.csv'):  # если файл существует
        with open('data.csv', 'r', encoding='utf-8') as csvfile2:  # ищем максимальный индекс в базе
            csv_reader_2 = csv.DictReader(csvfile2)
            max_id = 1
            for row in csv_reader_2:
                if max_id < int(row['id']):
                    max_id = int(row['id'])

        with open('data.csv', 'a+', encoding='utf-8', newline='') as csvfile3:  # Записываем контакт в базу
            fieldnames_2 = ['id', 'first_name', 'second_name', 'last_name', 'phone']
            csv_writer = csv.DictWriter(csvfile3, fieldnames=fieldnames_2)

            csv_writer.writerow({'id': max_id+1, 'last_name': surname,
                                'first_name': name, 'second_name': sec_name, 'phone': phone})
            
    else:  # если файл не существует
        with open('data.csv', 'w', encoding='utf-8', newline='') as csvfile3:
            fieldnames_3 = ['id', 'first_name', 'second_name', 'last_name', 'phone']
            csv_writer = csv.DictWriter(csvfile3, fieldnames=fieldnames_3)
            csv_writer.writeheader()  # записать заголовки
            max_id = 0

            csv_writer.writerow({'id': max_id+1, 'last_name': surname,
                                'first_name': name, 'second_name': sec_name, 'phone': phone})

    contact_1 = [max_id+1, name, surname, sec_name, phone]
    fieldnames_4 = ['id', 'first_name', 'second_name', 'last_name', 'phone']
    print('\nНовый контакт добавлен в базу:')
    v.show_book([fieldnames_4, contact_1])
    return contact_1
