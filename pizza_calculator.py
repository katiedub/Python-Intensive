"""
pizza_calculator.py
Implementation/Demo of using numerical inputs and utilizing mathematical operators
"""
# ask the user how many pizzas they want, how many toppings,
# and how many special toppings
# inputs
num_pizzas = int(input("How many pizzas would you like?"))
num_toppings = int(input("How many toppings?"))
num_special = int(input("How many special toppings?"))

# basic pizza -> $5
# regular topping -> $1.25
# special topping -> $ 1.75
# use math operations
pizza_cost = 5
topping_cost = 1.25
special_cost = 1.75

total = pizza_cost * num_pizzas + topping_cost * num_toppings + special_cost * num_special
# tell the user the total price
# this could include tax
# print
print("Your total comes to $ %.2f" % total)
