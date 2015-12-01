numbers = 5

def fact(num):
    output = 1
    for n in range(1, num + 1):
        output *= n
    return output
print (fact(numbers))

#ver2

def factorial(num):
    output = 1
    i = 1
    while i <= num:
        output *= i
        i += 1
    return output
print(factorial(6))
