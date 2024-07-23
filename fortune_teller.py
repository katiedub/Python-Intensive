"""
fortune_teller.py
An implementation of a fortune teller using nested conditionals

Example Output:
Please choose one of the following colors: blue, red, pink pink
Please choose a number between 1 and 3 1
Your fortune:
One day you will meet a genie who will grant you three wishes
"""

# input(), print(), int()
# ask the user for one of three colors
color = input("Pick a color: pink, blue, or purple \n")
# ask the user for one of three numbers
number = int(input("Pick a number between 1 and 3 \n"))

print("\nYour fortune:")             
# use if statements to return 9 unique fortunes based on color combinations
if color == "pink":
    if number == 1:
        print("You will have good luck today")
    elif number == 2:
        print("A new friendship will bring unexpected joy")
    else:
        print("A problem will not be as bad as it seems")
        
elif color == "blue":
    if number == 1:
        print("Be slow to speak and quick to act")
    elif number == 2:
        print("An old acquaintance will re-enter your life")
    else:
        print("Kind words may mean more than they seem")
        
# elif color == "purple":
else:
    if number == 1:
        print("The chase of gain is rich in hate")
    elif number == 2:
        print("Change your horizons if you want to change your luck")
    else:
        print("Recognition will come from unexpected sources")
