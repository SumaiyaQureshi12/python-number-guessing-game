import random

print("Welcome to the game, This is a Number Guessing Game!\nYou got 5 attempts to guess the number between 50 to 100, let's start the game")

number_to_guess = random.randrange(50, 100) 

chances = 5
guess_counter = 0

while guess_counter < chances:
    guess_counter += 1
    my_guess = int(input("Please enter your guess: "))

    if my_guess == number_to_guess:
        print(f"The number is {number_to_guess} and you found it right!! in the {guess_counter} attempt")
        break
    elif my_guess < number_to_guess:
        print("Your guess is very low, try again!")
    else:
        print("Your guess is very high, try again!")

# Agar 5 attempts ke baad bhi guess nahi mila
if my_guess != number_to_guess:
    print(f"Oops sorry, the number was {number_to_guess}. Better luck next time!")
