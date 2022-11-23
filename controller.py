import mod_add as ma
import mod_get_bd as mg
import view as v
def push_the_button():
    login = v.correct_name('Введите ваш Login : ')
    info = v.get_choice()
    if info == 1:
        print(ma.write_data())
    if info == 2:
        print(mg.get_base())