filename = 'alma.txt'
def print_file_lines_with_a(name):
    input_file = open(name)
    file_content = input_file.read()
    input_file.close()
    output = ''
    for line in file_content.split('\n'):
        output += 'a' + line
    return output
print(print_file_lines_with_a(filename))

#ver2

def print_file_lines_with_a2(name):
    file_to_print = open(name)
    lines = file_to_print.readlines()
    file_to_print.close()
    output = ''
    for line in lines:
        print('a' + line.rstrip())

print_file_lines_with_a2(filename)
