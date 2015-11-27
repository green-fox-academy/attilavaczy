

def reverse(in_list):
    reverse_list = []
    n = len(in_list)-1
    while n >= 0:
        reverse_list.append(in_list[n])
        n = n-1
    return reverse_list

output = reverse([1, 2, 3, 4])
print(output)
