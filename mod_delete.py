import csv
import view as v


def delete_confirm(list_d):
    with open('data.csv', 'r', encoding='utf-8') as csvfile_4:
        reader_choice = csv.reader(csvfile_4)
        list_choice = list(reader_choice)
        id_choice = [d[0] for d in list_choice]
        if len(list_d) > 1:
            while True:
                try:
                    id_num = int(input('Введите id записи, которую вы хотите удалить.. -> '))
                except ValueError:
                    print('Введено не число')
                if str(id_num) not in id_choice:
                    print('Такого индекса нет в базе')
                else:
                    break

            for row_2 in list_choice:
                if row_2[0] == str(id_num):
                    v.show_book([list_choice[0], row_2])
        else:
            id_num = list_d[0][0]

        if input('\nПодтвердите, что выбрана правильная запись для удаления. (y/n)').lower() in ['д', 'y', 'да', 'yes']:
            data_delete(id_num)


def data_delete(id_number):
    with open('data.csv', 'r', encoding='utf-8') as csvfile_6:
        reader_delete = csv.reader(csvfile_6.readlines())
        clean_rows = [row3 for row3 in reader_delete if row3[0] != str(id_number)]  # генератор всех строк, кроме той, которую указали

    with open('data.csv', 'w', encoding='utf-8', newline='') as csvfile_7:
        writer_record = csv.writer(csvfile_7)
        writer_record.writerows(clean_rows)
    print('\nЗапись удалена')
