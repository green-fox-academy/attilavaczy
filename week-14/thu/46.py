filename = 'alma.txt'
def print_file_lines_with_a(name):
    input_file = open(name)
    file_content = input_file.read()
    input_file.close()
    output = ''
    for line in content.split('\n'):
        output += 'a' + line
    return output
print(print_file_lines_with_a(filename))
