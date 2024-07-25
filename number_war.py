"""
number_war.py
Implementation of the war game.
"""
import random

# generate a list of 10 random integers between 0 and 100
# call it my_hand and display items in this list

# generate a list of 10 random integers between 0 and 100 for computer
# call this opp_hand
my_hand = []
opp_hand = []

# my_scores = 0
# opp_scores = 0
my_scores = []
opp_scores = []

for i in range(10):
    my_num = random.randint(0,100)
    opp_num = random.randint(0,100)
    my_hand.append(my_num)
    opp_hand.append(opp_num)

# test the hand generation using prints
# want to check they are the same length
# and that the values are different
# print(my_hand)
# print(opp_hand)


# player picks one of the items from my_hand to "battle"
# using indices, my_hand[]
round_num = 1
# WHILE LOOP
while len(opp_hand) > 0:
    print("\nRound", round_num)
    print("......................................")
    round_num +=1
    # USER TURN
    # print current state of the hand and ask player to select a card
    print("Here is your hand:\n \t", my_hand)
    play_id = int(input("What is the index of your selected card?\n"))
    # tell the player which true value they played
    my_play = my_hand[play_id]
    print("You played", my_play)

    # COMPUTER TURN
    # computer randomly picks one of the items from opp_hand
    # using indices, and length of the list
    opp_id = random.randint(0, len(opp_hand)-1)
    opp_play = opp_hand[opp_id]
    print("Computer played", opp_play)

    # i win
    if my_play > opp_play:
        print("You win this round :)")
        # move cards
        # my_scores += 1
        my_scores.append(my_hand.pop(play_id))
        my_scores.append(opp_hand.pop(opp_id))
    elif opp_play > my_play:
        print("Computer wins this round :(")
        # move cards
        # opp_scores += 1
        opp_scores.append(my_hand.pop(play_id))
        opp_scores.append(opp_hand.pop(opp_id))
    else:
        print("It's a tie :/")
        # move cards
        my_hand.pop(play_id)
        opp_hand.pop(opp_id)
    
    # print(my_scores)
    # print(opp_scores)

    # my_hand.pop(play_id)
    # opp_hand.pop(opp_id)

# the higher value wins, lower value loses, same value ties
# assign "cards" or points to the winner

# once you're through all of the hands you want to print the overall winner
print("\nFinal Stats!")
print("......................................")
print("Your winnings:", my_scores)
print("Computer winnings:", opp_scores)
if len(my_scores) > len(opp_scores):
  print("You win!")
elif len(opp_scores) > len(my_scores):
  print("You lose.")
else:
  print("You tie.")

