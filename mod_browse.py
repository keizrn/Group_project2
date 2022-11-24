import csv


def main_browse():
    try:
        with open('data.csv', 'r', encoding='utf-8', newline='') as csvfile_browse:
            reader_1 = csv.reader(csvfile_browse)
            return [row for row in reader_1]  # генератор по всей базе, вместе с заголовками
    except FileNotFoundError:
        return []
