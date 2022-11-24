def correct_name(text):
    name = input(f'{text} ')
    while True:
        if name.isalpha():
            return name.capitalize()
        print('не корректный ввод')
        name = input(f'{text} ')


def correct_number():
    number = input('Введите номер телефона +7 код номер без пробелов -> ')
    while True:
        if number[0] == '+' and number[1:].isdigit() : #and len(number) == 12:
            return number
        print('не корректный ввод')
        number = input('Введите номер телефона +7 код номер без пробелов -> ')

def get_choice():
    flag = False
    while not flag:
        try:
            number = int(input('Выберите действие:\n'
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

column_names = ['ID', 'name', 'surname', 'sec_name', 'phones']
mode = {0: 'None', 1: 'Имя', 2: 'Фамилия', 3: 'Отчество', 4: 'Телефон', 5: 'Удаление', 6: 'Просмотр'}
act = {1: 'Ввод данных', 2: 'Просмотр базы', 3: 'Поиск', 4: 'Внесение изменений', 5: 'Удаление записи', 6: 'Выход из программы'}
