import csv


def delete_confirm(list_d):
    with open('data.csv', 'r', encoding='utf-8') as csvfile_4:
        reader_choice = csv.reader(csvfile_4)
        list_choice = list(reader_choice)
        id_choice = [d[0] for d in list_choice]
        if len(list_d) > 1:
            input_id = True
            while input_id:
                try:
                    id_num = int(input('Введите id записи, которую вы хотите изменить.. -> '))
                    input_id = False
                except ValueError:
                    print('Введено не число')
            if str(id_num) not in id_choice:
                print('Такого индекса нет в базе')
        else:
            id_num = list_d[0][0]

        for row_2 in list_choice:
            if row_2[0] == str(id_num):
                print(row_2)
        if input('\nПодтвердите, что выбрана правильная запись для удаления. (д, y)').lower() in ['д', 'y', 'да', 'yes']:
            data_delete(id_num)
        else:
            return


def data_delete(id_number):
    with open('data.csv', 'r', encoding='utf-8') as csvfile_6:
        reader_delete = csv.reader(csvfile_6.readlines())
        clean_rows = [row3 for row3 in reader_delete if row3[0] != str(id_number)]

    with open('data.csv', 'w', encoding='utf-8', newline='') as csvfile_7:
        writer_record = csv.writer(csvfile_7)
        writer_record.writerows(clean_rows)
