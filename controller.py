import mod_add as ma
import logger as lg
import mod_browse as mb
import mod_search as ms
import mod_changes as mc
import mod_delete as md
import view as v


def push_the_button():
    login = v.correct_name('Введите ваш Login : ')
    while True:
        info = v.get_choice()  # Основное меню
        func = 0
        contact = []

        if info == 1:  # Ввод данных
            contact = ma.write_data()
            lg.write_log(info, login, contact, func)  # логгер

        elif info == 2:  # просмотр базы
            contact_2 = mb.main_browse()
            v.show_book(contact_2)  # вывод таблицы
            lg.write_log(info, login, 'ALL BD', func)

        elif info == 3:  # поиск по базе
            list_search = ms.search_data()  # функция поиска
            if list_search:  # если поиск успешный
                v.show_book(list_search)
            lg.write_log(info, login, list_search, func)
            if list_search and input('Внести изменения? (y/n)').lower() in ['д', 'y', 'да', 'yes']:  # спросить, внести ли изменения
                contact, func = mc.change_confirm(list_search)  # вносим изменения
            lg.write_log(info, login, contact, func)

        elif info == 4:  # Изменение данных
            list_search2 = ms.search_data()
            if list_search2:  # если непустой поиск
                v.show_book(list_search2)
                contact, func = mc.change_confirm(list_search2)  # вносим изменения
            lg.write_log(info, login, contact, func)

        elif info == 5:  # Удаление записи
            list_search3 = ms.search_data()
            if list_search3:  # если поиск успешный
                v.show_book(list_search3)
                md.delete_confirm(list_search3)  # функция удаления
            lg.write_log(info, login, list_search3, func)

        elif info == 6:
            lg.write_log(info, login, '', func)
            break

        else:
            print('Неправильный пункт меню')
            continue
