from datetime import datetime as dt
from view import mode, info

def write_log(tipe, login, contact, func):
    time = dt.now().strftime('%H:%M')
    with open ('db_log.txt', 'a', encoding='utf-8') as file:
        file.writelines(f'Время {time}, Пользователь {login}, Действия = {info[tipe]}, Результат = {contact}, Изменения = {mode[func]}\n')