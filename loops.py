"""
loops.py
An overview of different loops and iterations
"""

# definite loops-> for loops
# have a defined end, they go for a certain number of iterations
# know how many iterations at the start
for i in range(10):
    print(i)

# indefinite loops -> while loops
# don't have a defined end, you don't know exact number of iterations
# it will take to end the loop, depending on a boolean (T/F) the loop
# will keep iterating while the boolean is True
x = 0
while x < 10:
    print(x)
    print("loop")
    # x = x+1
    x += 1

print("loop complete")

x=0
while True:
    print("hi")
    x += 1
    if x == 10:
        break # can also break out of either loop with a break

# utilizing a random package
import random

# generate a random integer between 0 and 10 including the bounds
num1 = random.randint(0,10)

# generate a random float decimal number between 0.0000 and 0.9999
num2 = random.random()

print(num1)
print(num2)


# nested loops
for num in range(1,20):
    for i in range(2, num):
        if num%i == 0: # % remainder of num / i
            break
    else:
        print(num, "is prime")



            



