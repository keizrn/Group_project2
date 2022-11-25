import csv
import view as v


def search_data(file_name9):  # поиск данных в базе
    search_q = v.input_search_query()
    with open(f'{file_name9}.csv', 'r', encoding='utf-8') as csvfile_4:
        reader_search = list(csv.reader(csvfile_4))
        contacts_1 = [row for row in reader_search if search_q in row]
        if not contacts_1:
            v.text_err(8)  # информация не найдена
            return []
        else:
            contacts_1.insert(0, reader_search[0])
            return contacts_1
