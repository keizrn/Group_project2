import csv

import view as v
import mod_search


def change_confirm(list_s):
    if list_s is None:
        return None, 0
    else: 
        with open('data.csv', 'r', encoding='utf-8') as csvfile_4:
            reader_choice = csv.reader(csvfile_4)
            list_choice = list(reader_choice)
            id_choice = [d[0] for d in list_choice]
            if len(list_s) > 1:
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
                id_num = list_s[0][0]

            for row_2 in list_choice:
                if row_2[0] == str(id_num):
                    v.show_book([list_choice[0], row_2])
            if input('\nПодтвердите, что выбрана правильная запись. (y/n)').lower() in ['д', 'y', 'да', 'yes']:
                return data_change(id_num)
            else:
                return None, 0


def data_change(id_number):
    with open('data.csv', 'r', encoding='utf-8') as csvfile_6:
        dict_change = csv.DictReader(csvfile_6)
        header_change = dict_change.fieldnames

        reader_change = csv.reader(csvfile_6)
        list_change = list(reader_change)
        for row_3 in list_change:
            if row_3[0] == str(id_number):
                list_change_2 = row_3
        while True:
            print('\nВыберите запись, которую вы хотите изменить:')
            for i_3 in range(1, len(list_change_2)):
                print(f'{header_change[i_3]} - {list_change_2[i_3]} - {i_3}')
            try:
                choice_id = int(input('\nУкажите цифру ->  '))

                if choice_id == 1:
                    str_temp = input('Вы собираетесь изменить имя. Введите новое имя.. -> ')
                elif choice_id == 2:
                    str_temp = input('Вы собираетесь изменить отчество. Введите новое отчество.. -> ')
                elif choice_id == 3:
                    str_temp = input('Вы собираетесь изменить фамилию. Введите новую фамилию.. -> ')
                elif choice_id == 4:
                    str_temp = input('Вы собираетесь изменить номер телефона. Введите номер телефона +7 код номер без пробелов ->')
                else:
                    print('Неправильный пункт меню')
                    continue
                if input(f'Подтвердите перезапись в строке {id_number}: с {list_change_2[choice_id]} на {str_temp}. (y/n)').lower() in ['д', 'y', 'да', 'yes']:
                    record_change(id_number, str_temp, choice_id)
                    contact = f'Изменения в записи id {id_number}: с {list_change_2[choice_id]} на {str_temp}'
                    return contact, choice_id

            except ValueError:
                print('Введено не число')
                continue


def record_change(id_n, string_1, header_1):
    with open('data.csv', 'r', encoding='utf-8') as csvfile_6:
        reader_record = csv.reader(csvfile_6.readlines())

    with open('data.csv', 'w', encoding='utf-8', newline='') as csvfile_7:
        writer_record = csv.writer(csvfile_7)
        for line_6 in reader_record:
            if line_6[0] == str(id_n):
                line_6.pop(header_1)
                line_6.insert(header_1, string_1)
                writer_record.writerow(line_6)
                break
            else:
                writer_record.writerow(line_6)
        writer_record.writerows(reader_record)
