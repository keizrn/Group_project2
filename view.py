from tabulate import tabulate

dict_error = {0: '',
              1: 'Не корректный ввод\n',
              2: 'Введено не число\n',
              3: 'Неправильный пункт меню\n',
              4: 'Такого индекса нет в базе\n',
              } # словарь строк / сообщений об ошибках с ключами

column_names = ['ID', 'name', 'surname', 'sec_name', 'phones']
mode = {0: 'None', 1: 'Имя', 2: 'Фамилия', 3: 'Отчество', 4: 'Телефон', 5: 'Удаление', 6: 'Просмотр'}
act = {1: 'Ввод данных', 2: 'Просмотр базы', 3: 'Поиск', 4: 'Внесение изменений', 5: 'Удаление записи', 6: 'Выход из программы'}


def correct_name(text):  # Проверка на ввод имени/фамилии
    name = input(f'{text} ')
    while True:
        if name.isalpha():
            return name.capitalize()
        text_err(1) 
        name = input(f'{text} ')


def any_name(text):  # Проверка на ввод отчества
    name_2 = input(f'{text} ')
    while True:
        if name_2.isalpha() or name_2 == '-':
            return name_2.capitalize()
        text_err(1)
        name_2 = input(f'{text} ')

def correct_number():  # проверка на ввод номера телефона
    number = input('Введите номер телефона +7 код номер без пробелов -> ')
    while True:
        if number[0] == '+' and number[1:].isdigit():
            return number
        text_err(1)
        number = input('Введите номер телефона +7 код номер без пробелов -> ')


def get_choice():  # основное меню
    while True:
        try:
            number = int(input('\nВыберите действие:\n'
                               'Ввод данных - 1\n'
                               'Просмотр базы данных - 2\n'
                               'Поиск по базе - 3\n'
                               'Изменение данных - 4\n'
                               'Удаление записи - 5\n'
                               'Выход из программы - 6: '))
            if 0 < number < 7:
                break
        except ValueError:
            text_err(2)
    return number


def input_search_query():  # ввод значения для поиска
    return input('Введите значение для поиска.. ->  ').title()


def show_book(book_1: list):  # вывод таблицы
    headers_1 = book_1.pop(0)
    print(tabulate(book_1, headers=headers_1, tablefmt='fancy_grid'))

def choice_file_input():
    return input('- Введите название файла или путь к файлу с данными\n'
                 '- Или нажмите "Enter" для файла по умолчанию (data.csv).\n')

def text_err(num_1): 
    print(dict_error[num_1]) # вывод строки / сообщения об ошибке
