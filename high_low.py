"""
high_low.py
implementation of a number guessing game
"""
import random

# computer will generate a random positive integer between 0 and 100
answer = random.randint(0,100)

while True:
    # computer will ask the user to guess a number between 0 and 100
    # keep re-prompting until the user guesses the correct value
    guess = int(input("Guess a number between 0 and 100"))
    
    # if the guess is higher, tell the user
    if guess > answer:
        print("Too high, try again")

    # if the guess is lower, tell the user
    elif guess < answer:
        print("Too low, try again")

    # if the guess is correct, tell the user, break out of the loop
    if guess == answer:
        print("You got it!")
        break




# using the correct guess to define the loop
import random

# computer will generate a random positive integer between 0 and 100
answer = random.randint(0,100)

# must get an initial guess
guess = int(input("Guess a number between 0 and 100\n"))
while guess != answer:
    # computer will ask the user to guess a number between 0 and 100
    # keep re-prompting until the user guesses the correct value
    # if the guess is higher, tell the user
    if guess > answer:
        # in the loop give opportunity to guess again for both conditions
        guess = int(input("Too high, try again\n"))

    # if the guess is lower, tell the user
    elif guess < answer:
        # opportunity to change guess
        guess = int(input("Too low, try again\n"))

print("You got it!")





    
