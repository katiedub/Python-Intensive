"""
quiz.py

"""
print("Math Quiz!")
score = 0

# ask user 5 questions about any topic where the user can input an answer
# input
a1 = int(input("\n What is 10/2?"))

# after each question, tell the user whether or not their answer was correct
# if/ else to test whether it was correct, print
if a1 == 5:
    print("Nice job!")
    score = score + 1
else:
    print("Yikes, tough start")

# question 2
a2 = int(input("\n What is 2+2?"))
if a2 == 4:
    print("\t Nice")
    score = score + 1
else:
    print("\t Aw man, wrong answer.")

# question 3
a3 = int(input("\n What is 3**2?"))
if a3 == 9:
    print("\t Good job")
    score += 1
else:
    print("\t Yikes, tough luck")

# question 4
a4 = int(input("\n What is 4*5?"))
if a4 == 20:
    print("\t Awesome work")
    score += 1
else:
    print("\t Not quite")

# question 5
a5 = int(input("\n What is 15/3?"))
if a5 == 5:
    print("\t Finishing strong")
    score += 1
else:
    print("\t :(")

# at the end give the user a final score
# print, score in a variable
# depending the score, print some message "aw man you got them all wrong
print("\n Your score was", score,"/ 5.")
if score == 5:
    print("A perfect score!")
elif score == 0:
    print("Oof you missed them all.")
else:
    print("Room for improvement, but not bad!")


# formatting prints note
# \n new line
# \t tab











