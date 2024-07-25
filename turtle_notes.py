"""
turtle_notes.py

"""
from turtle import *

t = Turtle()

# changing shape and color of the turtle object
t.shape("turtle")
# arrow, circle, square
t.color("plum")

# moving our turtle object
# using functions
def star():
    t.left(36)
    for i in range(5):
        t.forward(100)
        t.left(144)

def square(size=100):
    for i in range(4):
        t.forward(size)
        t.left(90)

def shape(angle, size, sides, color):
    t.color(color)
    t.begin_fill()
    for i in range(sides):
        t.forward(size)
        t.left(angle)
    t.end_fill()
    
        
square()
square(200)
shape(90, 100, 4, "cadetblue")


colors = ["cadetblue", "chartreuse", "cyan", "firebrick",
          "paleturquoise", "limegreen"]

style = ("Comic Sans MS", 30, "bold")
t.color("deep pink")
t.write("katie", font= style, align = 'center')
    
