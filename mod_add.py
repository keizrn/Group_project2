import view as v
import csv
import os.path

def write_data():
    name = v.correct_name('\nВведите Имя : ')
    sec_name = v.any_name('Введите Отчество (если нет отчества "-"): ')
    surname = v.correct_name('Введите Фамилию : ')
    phone = v.correct_number()

    if os.path.exists('data.csv'):

        with open('data.csv', 'r', encoding='utf-8') as csvfile2:
            csv_reader_2 = csv.DictReader(csvfile2)
            max_id = 1
            for row in csv_reader_2:
                if max_id < int(row['id']):
                    max_id = int(row['id'])

        with open('data.csv', 'a+', encoding='utf-8', newline='') as csvfile3:
            fieldnames_2 = ['id', 'first_name', 'second_name', 'last_name', 'phone']
            csv_writer = csv.DictWriter(csvfile3, fieldnames=fieldnames_2)

            csv_writer.writerow({'id': max_id+1, 'last_name': surname,
                                'first_name': name, 'second_name': sec_name, 'phone': phone})
            
    else:
        with open('data.csv', 'w', encoding='utf-8', newline='') as csvfile3:
            fieldnames_3 = ['id', 'first_name', 'second_name', 'last_name', 'phone']
            csv_writer = csv.DictWriter(csvfile3, fieldnames=fieldnames_3)
            csv_writer.writeheader()
            max_id = 0

            csv_writer.writerow({'id': max_id+1, 'last_name': surname,
                                'first_name': name, 'second_name': sec_name, 'phone': phone})

    columns = [max_id+1, name, surname, sec_name, phone]
    fieldnames_4 = ['id', 'first_name', 'second_name', 'last_name', 'phone']
    print('\nНовый контакт добавлен в базу:')
    v.show_book([fieldnames_4, columns])
    contact = {}
    for i in range(len(columns)):
        contact[v.column_names[i]] = columns[i] if columns[i] else '-'
    return contact
