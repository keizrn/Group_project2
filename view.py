from tabulate import tabulate

column_names = ['ID', 'name', 'surname', 'sec_name', 'phones']
mode = {0: 'None', 1: 'Имя', 2: 'Фамилия', 3: 'Отчество', 4: 'Телефон', 5: 'Удаление', 6: 'Просмотр'}
act = {1: 'Ввод данных', 2: 'Просмотр базы', 3: 'Поиск', 4: 'Внесение изменений', 5: 'Удаление записи', 6: 'Выход из программы'}


def correct_name(text):
    name = input(f'{text} ')
    while True:
        if name.isalpha():
            return name.capitalize()
        print('не корректный ввод')
        name = input(f'{text} ')


def any_name(text):
    name_2 = input(f'{text} ')
    while True:
        if name_2.isalpha() or name_2 == '-':
            return name_2.capitalize()
        print('не корректный ввод')
        name_2 = input(f'{text} ')

def correct_number():
    number = input('Введите номер телефона +7 код номер без пробелов -> ')
    while True:
        if number[0] == '+' and number[1:].isdigit() : #and len(number) == 12:
        # if number[0] == number[1:6].isdigit():
            return number
        print('не корректный ввод')
        number = input('Введите номер телефона +7 код номер без пробелов -> ')


def get_choice():
    flag = False
    while not flag:
        try:
            number = int(input('\nВыберите действие:\n'
                               'Ввод данных - 1\n'
                               'Просмотр базы данных - 2\n'
                               'Поиск по базе - 3\n'
                               'Изменение данных - 4\n'
                               'Удаление записи - 5\n'
                               'Выход из программы - 6: '))
            if 0 < number < 7:
                flag = True
        except ValueError:
            print("Ошибка, попробуйте еще раз!")
    return number


def input_search_query():
    return input('Введите значение для поиска.. ->  ').title()


def show_book(book_1: list):
    headers_1 = book_1.pop(0)
    print(tabulate(book_1, headers=headers_1, tablefmt='fancy_grid'))
