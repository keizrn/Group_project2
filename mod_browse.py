import csv


def main_browse():
    try:
        with open('data.csv', 'r', encoding='utf-8', newline='') as csvfile_browse:
            dict_reader1 = csv.DictReader(csvfile_browse)
            header_1 = dict_reader1.fieldnames
            reader_1 = csv.reader(csvfile_browse)
            contacts_1 = [row for row in reader_1 if reader_1.line_num > 0]
            return header_1, contacts_1
    except FileNotFoundError:
        return []
