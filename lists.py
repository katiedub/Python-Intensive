"""
lists.py
An overview of lists in python!
"""

# lists
# can store objects of different data types in a list, can grow and shrink in size pretty easily

my_list = [] # empty list

my_list = ["item1", "item2", 3, True, 5.93]

# list index [n]
print(my_list[0]) # indexing into first item in a list
print(my_list[-1]) # indexing reverse direction to get last element
print(my_list[len(my_list)-1]) # another way to get last element

# know the object you're looking for but not the position
# call .index() method with the object as the argument in the parentheses
print(my_list.index("item1"))
print(my_list.index(3))


# how many elements are in a list len()
print(len(my_list))

# iterating through a list with a for loop
for var in my_list:
    print(var)

num_list = [1, 12, 33, 400]

number_sum = 0
for num in num_list:
    number_sum += num

print(number_sum)


# searching for existence of an element in a list using the in operator
names = ["Atticus", "Cooper", "Sam", "Yumio"]
if "Katie" in names:
    print("Found Katie")

if "Yumio" in names:
    print("Found Yumio")


# duplicates
set_list = ["bird", "john", "dog", "dog"]
unique = set(set_list)
# set = {"bird", "john", "dog"}
# can cast a set back into a list data type
unique_list = list(unique)


# list methods
# ways to alter a list
methods_ex = ["append", "insert", "extend", "index")

elem = "new_element"
index = 1
# add a single element to the end of a list
methods_ex.append(elem)

# inserting an element at a given index and shifting everything to the right
methods_ex.insert(index, elem)

# add the elements of another list to the end of a list
ex_2 = ["Atticus", "Cooper"]
methods_ex.extend(ex_2)

# returns the index number where the element is found
methods_ex.index(elem)

# finds the first instance of an element and removes it
methods_ex.remove(elem)

# in-place sort
methods_ex.sort()

# reverse the order of a list
methods_ex.reverse()

# removes and returns an element at a given index
methods_ex.pop(index)

# slice into a list, so grabbing a set of positions in the list
methods_ex[0:5]












