"""
text_adventure.py

"""

# player
# some number of choices to make
# various outcomes depending on those choices
# if/else conditionals

# use try: except: to encourage valid answers or always have an else case that pushes forward

# keep an inventory in a list
#Write a story with at least two endings....

bag = []

print("Welcome to my adventure!")

choice = input("Do you pick up a sword or a bag of chips? ")
if choice == "sword":
  bag.append("sword")
else:
  bag.append("chips")

print("There is a dragon")

choice2 = input("Do you fight it or offer it some chips? ")
if choice2 == "fight":
  if "sword" in bag:
    print("You defeat the dragon and pick up his treasures")
    bag.append("gold")
  else:
    print("The dragon ate you and your chips")
    bag.remove("chips")
else:
  if "chips" in bag:
    print("The dragon ate your chips and says good thing you didn't fight me with a sword. I was hungry and would have eaten you!")
    bag.remove("chips")
  else:
    print("The dragon ate you since you didn't have any chips")

print("Your ending bag:", bag)
