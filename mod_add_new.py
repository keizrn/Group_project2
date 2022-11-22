import model 

def get_contact(): 
    name = input('Введите имя: ')
    while not name:
        name = input('Это обязательное поле для заполнения. Повторите попытку: ')
    surname = input('Введите фамилию: ')
    additional_phones = True
    phones = input('Введите номер телефона: ')
    while not phones:
        phones = input('Это обязательное поле для заполнения. Повторите попытку: ')
    while additional_phones:
        reply = input('Введите дополнительный номер телефона. Для выхода введите прочерк "-": ')
        while not reply:
            reply = input('Вы ничего не ввели. Повторите попытку или нажмите прочерк "-" для выхода: ')
        if reply == '-':
            additional_phones = False
        else:
            phones += f'; {reply}'
    additional_e_mails = True
    e_mails = input('Введите email: ')
    while additional_e_mails:
        reply = input('Введите дополнительный e-mail. Для выхода нажмите процерк "-": ')
        while not reply:
            reply = input('Вы ничего не ввели. Повторите попытку или нижмите прочерк "-" для выхода: ')
        if reply == '-':
            additional_e_mails = False
        else:
            e_mails += f'; {reply}'

    columns = [name, surname, phones, e_mails]
    contact = {}
    for i in range(len(columns)):
        contact[model.column_names[i]] = columns[i] if columns[i] else '-'
    return contact