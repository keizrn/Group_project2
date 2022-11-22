import mod_add as m
import view as v
def push_the_button():
    login = v.correct_name('Введите ваш Login : ')
    info = v.get_choice()
    if info == 1:
        m.write_data()
