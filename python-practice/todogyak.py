from todogyak_func import *

def menu_test():
    print('\nMenu:\n 1. Add \n 2. Remove \n 3. Current list \n 0. Exit')

def main_menu():

    while True:
        menu_test()
        user_input = int(input('Choose one: '))
        if user_input == 1:
            print('Add')
        elif user_input == 2:
            print('Remove')
        elif user_input == 3:
            print('\nCurrent list')
            get_list(read_db())
        elif user_input == 0:
            return False
main_menu()
