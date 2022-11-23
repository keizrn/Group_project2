import mod_add as ma
# import mod_get_bd as mg
import mod_browse as mb
import mod_search as ms
import mod_changes as mc
import mod_delete as md
import view as v


def push_the_button():
    while True:
        login = v.correct_name('Введите ваш Login : ')
        info = v.get_choice()
        if info == 1:
            print(ma.write_data())
        elif info == 2:
            print(mb.main_browse())
        elif info == 3:

            list_search = ms.search_data()
            print(list_search)
            if list_search and input('Внести изменения? (д, y)').lower() in ['д', 'y', 'да', 'yes']:
                mc.change_confirm(list_search)
        elif info == 4:
            list_search2 = ms.search_data()
            print(list_search2)
            mc.change_confirm(list_searc2)
        elif info == 5:
            list_search3 = ms.search_data()
            print(list_search3)
            md.delete_confirm(list_search3)
        elif info == 6:
            break

        else:
            print('Неправильный пункт меню')
            continue
