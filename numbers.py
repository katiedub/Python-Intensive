"""
numbers.py
"""
import random

num_list = []
# generate a list of 5 random integers between 1 and 100 called num_list
for i in range(5):
    num_list.append(random.randint(1, 100))

# allow the user to input 5 integers of their choosing between 1 and 100 as bets
# save these in a length 5 list called my_nums
my_nums = []
while len(my_nums) < 5:
    num = input("Pick a number\n")
    try: # ensures that the value is an integer
        num = int(num)
        if num >= 1 and num <= 100: # ensures the value is in the range
            my_nums.append(num)
        else:
            print("This number is not in the range")
    except:
        print("Invalid input, please enter an integer")
    
# compare your list to the computer list to see how many numbers in your list
# were accurate predictions/in the computer list
correct_count = 0
for num in my_nums:
    if num in num_list:
        correct_count += 1

# tell the user how many they guessed correctly and reveal the computer numbers
# at the end
print("You guessed", correct_count, "of the numbers correctly.")
print("The winning numbers were the following:")
print(num_list)
print("Your final guesses were:")
print(my_nums)
