names = ['Zakarias', 'Hans', 'Otto', 'Ole']

def shortest_name_list(names_list):
    output = names_list[0]
    for n in names_list:
        if len(n) < len(names_list):
            output = n
    return output
print(shortest_name_list(names))
