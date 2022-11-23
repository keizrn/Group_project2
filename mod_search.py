import csv

def search_data(search_q):
    with open('data.csv', 'r', encoding='utf-8') as csvfile_4:
        reader_search = csv.reader(csvfile_4)
        is_found = False
        for row in reader_search:
            if search_q in row:
                print(row)
                is_found = True
                break
        if not is_found:
            return print("Информация не найдена")
