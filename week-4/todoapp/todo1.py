from operations import *

def main():
    database = read_db('database.txt')
    print(database)

    while True:
        show_menu()
        user_input = int(input('Choose something: '))

        if user_input == 1:
            add_task(database)

        if user_input == 2:
            delete_elements(database)

        elif user_input == 0:
            break

    save_to_db(database, 'database.txt')
    print('Saved!')
main()
