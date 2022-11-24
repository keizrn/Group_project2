import csv
import mod_add as ma


def main_browse(file_name2):
    with open(f'{file_name2}.csv', 'r', encoding='utf-8', newline='') as csvfile_browse:
        reader_1 = csv.reader(csvfile_browse)
        return [row for row in reader_1]  # генератор по всей базе, вместе с заголовками
