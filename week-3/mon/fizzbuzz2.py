a = 0

while a < 100:
    a = a + 1
    if '3' in str(a):
        print("Fizz")
    elif '5' in str(a):
        print("Buzz")
    elif '3' or '5' in str(a):
        print("Fizzbuzz")
    else:
        print(a)
