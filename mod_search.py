import csv
import view as v


def search_data():
    search_q = v.input_search_query()
    with open('data.csv', 'r', encoding='utf-8') as csvfile_4:
        reader_search = csv.reader(csvfile_4)
        contacts_1 = [row for row in reader_search if search_q in row]
        if not contacts_1:
            return print("Информация не найдена")
        else:
            return contacts_1
