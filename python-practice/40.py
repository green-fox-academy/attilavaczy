numbers = [7, 5, 7, -1]

def get_minimum_from_numbers_list(number_list):
    output = number_list[0]
    for n in number_list:
        if output > n:
            output = n
    return output
print(get_minimum_from_numbers_list(numbers))
