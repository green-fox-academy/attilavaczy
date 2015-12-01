def factorial3(num):
    if num == 1:
        return 1
    else:
        return factorial3(num -1) * num

print(factorial3(3))
