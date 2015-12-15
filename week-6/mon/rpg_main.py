from rpg_naked import *

def main():
    menu = Menu(menu_items)
    load_menu = Menu(load_items)
    while True:
        menu.show_list()
        user_input = int(input('Choose from menu: '))
        if user_input == 2:
            load_menu.show_list()
        menu.number_select(user_input)
main()
