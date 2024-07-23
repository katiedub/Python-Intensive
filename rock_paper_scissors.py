"""
rock_paper_scissors.py
Implementation of a computer vs user rock, paper, scissors game
"""
import random
mode = int(input("Choose a game mode: \n\t1) For best of 3 \n\t2) For best of 5\n"))
if mode == 1:
    n_wins = 
# user input a choice or rock paper or scissors
play = input("Rock, paper, or scissors?\n")
# play = int(input("Choose a number: 1 for rock, 2 for paper, 3 for scissors\n"))
print() # using this line as a spacer in my output

user_num = 0
# will break out of this loop once a play is typed in accurately
while user_num == 0:
    if play == "rock":
        user_num = 1
    elif play == "paper":
        user_num = 2
    elif play == "scissors":
        user_num = 3
    else:
        # if play variable is not assigned 1,2, or 3
        # there must be an invalid input, so we give an opportunity to try again
        play = input("You must have a typo, try again.")

# computer select a number to represent rock paper or scissors
computer_num = random.randint(1,3)

# i could print out computer picked rock...
if computer_num == 1:
    print("Computer picked rock")
elif computer_num == 2:
    print("Computer picked paper")
else:
    print("Computer picked scissors")

# depending on the user choice and the random computer choice,
# output You win, you lose, or you tie
if user_num == 1:
    if computer_num == 2:
        # rock, paper
        print("You lose")
    elif computer_num == 3:
        # rock, scissors
        print("You win")
elif user_num == 2:
    if computer_num == 1:
        print("You win")
    elif computer_num == 3:
        print("You lose")
elif user_num == 3:
    if computer_num == 1:
        print("You lose")
    elif computer_num == 2:
        print("You win")
elif user_num == computer_num:
    print("It's a tie")


# extra challenge: ask the user how many games they wanna play like 3 or 5, etc
# game ends when they have the majority of wins
