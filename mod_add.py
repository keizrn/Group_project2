import view as v
import csv



def write_data():
    name = v.correct_name('Введите Имя : ')
    surname = v.correct_name('Введите Фамилию : ')
    sec_name = v.correct_name('Введите Отчество : ')
    phone = v.correct_number()

    with open('data.csv', 'a+', encoding='utf-8', newline='') as csvfile:
        fieldname = ['first_name', 'second_name', 'last_name', 'phone']
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldname)

        # csv_writer.writeheader()
        csv_writer.writerow({'last_name': surname,
        'first_name': name, 'second_name': sec_name, 'phone': phone})
