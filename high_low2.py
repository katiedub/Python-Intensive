"""
high_low2.py
implementation of a number guessing game with limited guess 
"""
import random

# computer will generate a random positive integer between 0 and 100
answer = random.randint(0,100)

print("Guess 1:")
guess = int(input("Guess a number between 0 and 100\n"))

# after initial guess, have 9 tries to get it right
for i in range(9):
    print("Guess", i+2,":")
    # if the guess is correct, tell the user, break out of the loop
    if guess == answer:
        print("You got it!")
        break
    # computer will ask the user to guess a number between 0 and 100    
    # if the guess is higher, tell the user
    elif guess > answer:
        guess = int(input("Too high, try again\n"))

    # if the guess is lower, tell the user
    elif guess < answer:
        guess = int(input("Too low, try again\n"))

    
    





    
