my_nums = []
while len(my_nums) < 5:
    num = input("Pick a number")
    try:
        num = int(num)
        if num >= 1 and num <= 100:
            my_nums.append(num)
        
    except:
        print("Invalid input, please enter an integer")
    

print(my_nums)
