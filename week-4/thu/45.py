filename = 'alma.txt'
def print_file(name):
    input_file = open(name)
    file_content = input_file.read()
    input_file.close()
    return file_content
print(print_file(filename))
