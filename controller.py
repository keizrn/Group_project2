import mod_add as ma
# import mod_get_bd as mg
import mod_browse as mb
import mod_search as ms
import view as v
def push_the_button():
    login = v.correct_name('Введите ваш Login : ')
    info = v.get_choice()
    if info == 1:
        print(ma.write_data())
    elif info == 2:
        print(mb.main_browse())
    elif info == 3:
        print(ms.search_data(input('Введите поисковый запрос(точный!): -> ')))
