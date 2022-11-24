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
        info = v.get_choice()
        func = 0
        if info == 1:
            contact = ma.write_data()
            print(contact)
            lg.write_log(info, login, contact, func)
        elif info == 2:
            contact = mb.main_browse()
            print(mb.main_browse())
            lg.write_log(info, login, contact, func)
        elif info == 3:

            list_search = ms.search_data()
            print(list_search)
            lg.write_log(info, login, list_search, func)
            if list_search and input('Внести изменения? (y/n)').lower() in ['д', 'y', 'да', 'yes']:
                contact, func =  mc.change_confirm(list_search)
                lg.write_log(info, login, contact, func)

        elif info == 4:
            list_search2 = ms.search_data()
            print(list_search2)
            contact, func = mc.change_confirm(list_search2)
            lg.write_log(info, login, contact, func)
        elif info == 5:
            list_search3 = ms.search_data()
            print(list_search3)
            md.delete_confirm(list_search3)
            lg.write_log(info, login, list_search3, func = 5)
        elif info == 6:
            contact = 'None'
            lg.write_log(info, login, contact, func)
            break

        else:
            print('Неправильный пункт меню')
            continue
