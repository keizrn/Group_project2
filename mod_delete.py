import csv

def data_delete():
    surname = input('Введите фамилию человека, контакт которого надо удалить.').title()
    with open('data.csv', 'r', encoding='utf-8') as csvfile_5:
            newrows = []
            contact_in_data = True
            reader = csv.reader(csvfile_5)
            for row in reader:
                if surname not in row:
                     newrows.append(row)
            else: 
                contact_in_data = False

    with open('data.csv', 'w', encoding='utf-8') as csvfile_6:
        fieldnames_6 = ['id', 'first_name', 'second_name', 'last_name', 'phone']
        writer = csv.DictWriter(csvfile_6, fieldnames=fieldnames_6)
        for row in newrows:
            writer.writerow(row)
    
    if contact_in_data:
        print (f'Контакт {surname} удален.')
    else: 
        print (f'Контакт {surname} не найден.')