import mod_add as ma
import logger as lg
import view as v
import mod_find as md

def push_the_button():
    login = v.correct_name('Введите ваш Login : ')
    type = v.get_choice()
    func = 0
    if type == 1:
        contact = ma.write_data()
        lg.write_log(type, login, contact, func)
        print(contact)
    if type == 2:
        print(md.search_data())