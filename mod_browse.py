import csv


def main_browse():
    try:
        with open('data.csv', 'r', encoding='utf-8', newline='') as csvfile_browse:
            reader_1 = csv.reader(csvfile_browse)
            contacts_1 = [row for row in reader_1]
            return contacts_1
    except FileNotFoundError:
        return []
