"""

Create a program that will draw a crazy pattern using the turtle.

Create lists for the path that Tina will take, the angles 
she will turn, and the colors she will use. The access those
lists to draw the pattern.

hint: all of your lists should have the same number of elements.
Review the ' Using Lists' section of the previous lesson if you need 
more help

"""

import random
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast. 


forwards = [50,100,25,235,234,25,123,152,3,25,23,25,50,100,25,23,52,51,42,52,23,125,232,52]
lefts = [50,100,25,23,52,51,42,52,23,125,232,52,50,100,25,23,52,51,42,52,23,125,232,52]
colors = [
    'red','green','blue','green','purple','red','green','blue','green','purple','red','green','red','green','blue','green','purple','red','green','blue','green','purple','red','green'
]


for i in range(len(colors)):

    tina.color(colors[i])
    tina.forward(forwards[i])
    tina.left(lefts[i])

    

turtle.exitonclick()  

