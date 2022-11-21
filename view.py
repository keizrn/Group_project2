from tabulate import tabulate


errors_1 = {0: '\n',
            1: 'Ошибка выбора меню\n'}

def view_menu():
    print("Выберите пункт меню:\n"
          "1 - Посмотреть таблицу\n"
          "2 - Добавить запись\n"
          "3 - Удалить запись\n"
          "4 - Редактировать запись\n"
          "5 - Выход\n\n->  ")


def browse_book(book_0: list) -> None:
    for contact in book_0:
        contact[-1] = contact[-1].replace(';', '\n')
    headers = ['id', 'Имя', 'Фамилия', 'Дата рождения', 'Место работы', 'Телефоны']
    print(tabulate(book_0, headers=headers, tablefmt='fancy_grid'))


def print_line(code_error):
    print(errors_1[code_error])
