import random

def random_number(i):
    """Random num game."""
    numbers = list(range(1,10))
    get_num = int(random.choice(numbers))
    guess = int(input(f"Try to guess a number between 1 and {i}: "))
    while guess != get_num:
        if guess > get_num:
            print("Too high. Try again: ")
            guess = int(input("What's your new guess? > "))
        elif guess < get_num:
            print ("Too low. Try again: ")
            guess = int(input("What's your new guess? > "))

    print(f"Nice! You guessed the right number. Correct answer {get_num}.")
    again = (input("Would you like to play again? Y/N: "))

    if again.lower() == 'y':
        guess = int(input(f"Try to guess a number between 1 and {i}: "))

random_number(10)


