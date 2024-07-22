"""
greetings.py
this has input, print, and variables
"""

# print three lines of code introducing yourself
# print("My name is Katie")
# print("I have blonde-ish hair")
# print("My favorite animal is a giraffe")

# data types and variables
x = 1
# y = str(1)
# "1"
# print(x+y)


# operators in python, math essentially
# instead of ^ for exponent **
# print(3*1**3)

# functions

# print is a built-in python function
print("my variable x is " + str(x) +".")
# using comma to concatenate can make the data types less picky
print("x",x)

#%s string
#%d decimals
name = "penguin"
print("my name is %s" % name)

y = 5
print("My favorite number is %d" % y)
# specify you want two digits after the decimal
print("Your total is %.2f dollars" % x)

# input
name = input("What is your name?")

# printing a statement that includes the name variable 
print("Hi", name, ", nice to meet you!")

# accepting a numerical input
age = int(input("what is your age?"))


print(age+1)














