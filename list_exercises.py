"""
list_exercises.py
"""
import random
# Generate a list of 100 random integers between -100 and 100
# duplicates are allowed, save it as mylist, print
print("Exercise 1")
mylist = []
for i in range(100):
    mylist.append(random.randint(-100,100))
print(mylist, "\n")

# sort mylist from lowest to highest and print it
print("Exercise 2")
mylist.sort()
print(mylist, "\n")

# sort mylist from highest to lowest and print it
print("Exercise 3")
mylist.reverse()
print(mylist, "\n")

# Create a sublist of all positive numbers from mylist called positive_list including 0
# print positive_list
print("Exercise 4")
positive_list = []
negative_list = []
for val in mylist:
    if val > 0:
        positive_list.append(val)
    else:
        negative_list.append(val)
print(positive_list, "\n")

# Create a sublist of all the negative numbers from mylist called negative_list (not including zero)
# print negative_list
print("Exercise 5")
print(negative_list, "\n")

# Create a list that removes all duplicates called unique_list
# print it
print("Exercise 6")
unique_list = list(set(mylist))
print(unique_list, "\n")

# Count the number of duplicates in the original mylist and
# print the number of duplicates
print("Exercise 7")
print(len(mylist)-len(unique_list), "\n")


# write a program that finds the largest number in a new list
# without using .sort()
print("Challenge 1")
new_list = []
for i in range(100):
    new_list.append(random.randint(-100,100))
    
max_val = -200 # arbitrary value lower than all possibilities
for val in mylist:
    if val > max_val:
        max_val = val
print(max_val)


# write a program that finds all the prime numbers in a range of numbers
# if n = 100, should output all prime numbers between 0 and 100
print("Challenge 2")
n = 300
prime_nums = []
# loop through integers in range
for num in range(1,n):
    # loop through numbers from 2 to that integer
    for i in range(2,num):
        # use % to determine if current number is a factor
        # if a factor is found, break out of the inner loop
        if num % i == 0:
            break
    else:
        print(num, "is prime")
        prime_nums.append(num)
    # else executes at the end of the inner loop
    # (only gets here if none of the numbers are factors)

print(prime_nums)
    
