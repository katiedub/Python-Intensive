"""
conditionals.py
"""
# syntax for conditionals
# < less than
# <= less than or equal to
# == equal to
# >= greater than or equal to
# > greater than
# != not equal to

print(1==2)
print(4<5)

# if statements
# example take user input for age,
# and reply with a statement saying whether or not they can drive
age = int(input("What is your age?"))

if age < 16:
    print("You are too young to drive.")
else:
    print("Cool, you can drive.")

if age > 18:
    print("You are old enough to vote.")
elif age > 16:
    print("You can't vote but at least you can drive.")
else:
    print("You're too young to vote or drive, sorry :(")


print("horse" == "horse")
