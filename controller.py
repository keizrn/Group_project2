import mod_add as ma
import logger as lg
import mod_browse as mb
import mod_search as ms
import mod_changes as mc
import mod_delete as md
import view as v
import os.path as os

file_1 = ''

def main_menu():
    login = v.correct_name('Введите ваш Login : ')
    while True:
        info = v.get_choice()  # Основное меню
        func = 0
        contact = []

        if info == 1:  # Ввод данных
            contact = ma.write_data(file_1)
            lg.write_log(info, login, contact, func)  # логгер

        elif info == 2:  # просмотр базы
            contact_2 = mb.main_browse(file_1)
            if contact_2:
                v.show_book(contact_2)  # вывод таблицы
            lg.write_log(info, login, 'ALL BD', func)

        elif info == 3:  # поиск по базе
            list_search = ms.search_data(file_1)  # функция поиска
            if list_search:  # если поиск успешный
                v.show_book(list_search)
            lg.write_log(info, login, list_search, func)
            if list_search and input('Внести изменения? (y/n)').lower() in ['д', 'y', 'да', 'yes']:  # спросить, внести ли изменения
                contact, func = mc.change_confirm(file_1, list_search)  # вносим изменения
            lg.write_log(info, login, contact, func)

        elif info == 4:  # Изменение данных
            list_search2 = ms.search_data(file_1)
            if list_search2:  # если непустой поиск
                v.show_book(list_search2)
                contact, func = mc.change_confirm(file_1, list_search2)  # вносим изменения
            lg.write_log(info, login, contact, func)

        elif info == 5:  # Удаление записи
            list_search3 = ms.search_data(file_1)
            if list_search3:  # если поиск успешный
                v.show_book(list_search3)
                md.delete_confirm(file_1, list_search3)  # функция удаления
            lg.write_log(info, login, list_search3, func)

        elif info == 6:
            lg.write_log(info, login, '', func)
            break

        else:
            v.text_err(3)
            continue


def file_path():
    global file_1
    file_1 = v.choice_file_input()
    if file_1 == '':
        file_1 = 'data'
    if not os.exists(f'{file_1}.csv'):
        if input('Файл не найден. Создать? (y/n)').lower() in ['д', 'y', 'да', 'yes']:  # спросить, создать ли файл
            ma.create_file(file_1)
        else:
            exit()
    main_menu()
