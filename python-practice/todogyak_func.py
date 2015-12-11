def read_db():
    n = open('db.txt', 'r')
    text = n.read()
    split_text = text.split()
    return split_text

def get_list(list):
    for index, value in enumerate(list):
        print(index + 1, value)

#get_list(read_db())
