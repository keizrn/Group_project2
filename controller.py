import view
import logger
import mod_add_new
import mod_browse

def start():
    run_program = True
    while run_program:
        try:
            mode_menu = input(view.view_menu())
            if mode_menu == '1':
                phonebook_2 = mod_browse.main_browse()
                if not phonebook_2:
                    view.print_line(1)
                else:
                    # logger
                    view.browse_book(phonebook_2)

            elif mode_menu == '2':
                mod_add_new.___
            else:
                view.print_line(1)

        except ValueError:
            view.print_line(1)
