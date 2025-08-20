# computer generates a random number
# user have to guess the number
# if the guessed number is lower than the actual number it will say "higher"
# if the guessed number is higher than the actual number it will say "lower"
# if the guessed number is equal to the actual number it will say "correct"
# lesser the guesses better the user plays

import random

computer_number = random.randint(1, 100)
user_guess = None
guess_count = 0

while user_guess != computer_number:
    user_guess = int(input("Guess the number (between 1 and 100): "))
    guess_count += 1

    if user_guess < computer_number:
        print("Higher!")
    elif user_guess > computer_number:
        print("Lower!")
    else:
        print("Correct!")

print(f"You guessed the number in {guess_count} tries!")