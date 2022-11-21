import csv


def main_browse():
    try:
        with open('phone_book.csv', 'r', encoding='utf-8', newline='') as csvfile_browse:
            reader_1 = csv.reader(csvfile_browse)
            contacts_1 = sorted([row for row in reader_1])
            return contacts_1
    except FileNotFoundError:
        return []
