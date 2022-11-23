import csv


def data_changes():
    with open('data.csv', 'r', encoding='utf-8', newline='') as csvfile3:
        csv_reader_3 = csv.reader(csvfile3)
        rows = list(csv_reader_3)

    print('Выбор параметра для поиска контакта.')
    for i in range (len(rows[0])):
        print(f'{i} - {rows[0][i]}')
    identificator_col = int('Введите номер выбранного параметра.')
    identificator = input('Введите данные для поиска.')
    
    for i in rows:
        if i[identificator_col] == identificator:
            isFound = True
            print('Выбор параметра для внесения изменений.')
            for j in range (len(rows[0])):
                print(f'{j} - {rows[0][j]}')
            modifying_col = int(input('Введите номер выбранного параметра.'))
            print(f'Текущие данные: {i[modifying_col]}')
            new_value = input(f'Введите новые данные.')
            old_value = i[modifying_col]
            i[modifying_col] = new_value
        else:
            isFound = False
    
    with open('data.csv', 'w', encoding='utf-8', newline='') as csvfile3:
        csv_writer = csv.writer(csvfile3, delimiter=',')
        csv_writer.writerow(rows)
    if isFound:
        return ('Изменения внесены.')
    else:
        return ('Запись не найдена.')