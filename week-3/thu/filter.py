numbers = [1, 2, 3, 4, 5, 6, 7, 8]
output = []

for n in numbers:
    if n % 2 == 0:
        output.append(n)

print(output)

#ver2

i = 0
while i < len(numbers):
    if numbers[i] % 2 == 0
        output.append(numbers[i])
    i += 1

print(output)

#ver3

def filter_even():
    for n in numbers:
        if n % 2 == 0:
            output.append(n)


filter_even()

print(output)

#ver4 (without output)

def filter_even(unfiltered_list):
    output = []
    for n in numbers:
        if n % 2 == 0:
            output.append(n)
    return output

filter_even(numbers)

print(output)
