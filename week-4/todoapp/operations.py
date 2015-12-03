
def raw_text_to_list(text):
    list_ = text.split('\n')
    return [string for string in list_ if string != '']

def list_to_raw_text(list_):
    return "\n".join(str(i) for i in list_)

def read_db(path):
    database = open(path, 'r')
    content = database.read()
    db_list = raw_text_to_list(content)
    database.close()
    return db_list

def save_to_db(database, path):
    db = open(path, 'w')
    text = list_to_raw_text(database)
    print(text)
    db.write(text)
    db.close()

def add_task(database):
    user_input = input('New task: ')
    database.append(user_input)
    print(database)

def delete_elements(database):
    user_input = input('Delete elements: ')
    del database[int(user_input)-1]
    print(database)


def show_menu():
    print('\nMenu:\n1.', 'Add\n2.', 'Delete\n0.', 'Exit and save\n')



def print_db(database):
    print(database)
#print_items()
