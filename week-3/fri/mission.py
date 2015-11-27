my_argument = input("Enter a word: ")

def reverse (uborka):
    palindrome = ''
    for n in my_argument:
        palindrome = n + palindrome
    print(my_argument+palindrome)

reverse(my_argument)
