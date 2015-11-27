from random import randint

def get_integer():
    number = int(input("Enter an integer:"))
    return number

number_to_guess = randint(0, 10)

number_of_guesses = 5

while number_of_guesses > 0:
    try:
        guess = get_integer()
    except ValueError:
        print("You entered a wrong value.")
    else:
        if number_to_guess == guess:
            print("Köszi")
            break
        elif number_to_guess > guess:
            print("Nagyobbra gondoltam")
            number_of_guesses -= 1
        else:
            print("Kisebbre gondoltam")
            number_of_guesses -= 1
