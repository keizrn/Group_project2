import csv

def search_data(last_name):
    with open('data.csv', 'r', encoding='utf-8') as csvfile_4:
        reader = csv.DictReader(csvfile_4)
        is_found = False
        for row in reader:
            # print(row[2])
            if row[2] == last_name:
                return print(f' {row[0]} - {row[1]} {row[2]} {row[3]} {row[4]} {row[5]}')
                is_found = True
                break
        if not is_found:
            return print("Информация не найдена")