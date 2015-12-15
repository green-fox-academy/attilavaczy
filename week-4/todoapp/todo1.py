from rpg_naked import *

def main():
    while True:
        menu = Menu(menu_items)
        menu.show_list()
        user_input = int(input('Hubbabubba: '))
        menu.number_select(user_input)
main()
