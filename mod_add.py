import view as v
import csv



def write_data():
    name = v.correct_name('Введите Имя : ')
    surname = v.correct_name('Введите Фамилию : ')
    sec_name = v.correct_name('Введите Отчество : ')
    phone = v.correct_number()

    with open('data.csv', 'r', encoding='utf-8') as csvfile2:
        csv_reader_2 = csv.DictReader(csvfile2)
        max_id = 1
        for row in csv_reader_2:
            if max_id < int(row['id']):
                max_id = int(row['id'])

    with open('data.csv', 'a+', encoding='utf-8', newline='') as csvfile3:
        fieldname_3 = ['id', 'first_name', 'second_name', 'last_name', 'phone']
        csv_writer = csv.DictWriter(csvfile3, fieldnames=fieldname_3)

        # csv_writer.writeheader()
        csv_writer.writerow({'id': max_id+1, 'last_name': surname,
                              'first_name': name, 'second_name': sec_name, 'phone': phone})
