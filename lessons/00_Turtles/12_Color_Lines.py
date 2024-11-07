"""
Color Lines

1) Finish the program to make Tina draw a square with each side being a different color. 

"""

import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(90)                           # Make the turtle move as fast, but not too fast. 
colors = [ 'red', 'blue', 'purple', 'orange']    # define a list of colors
tina.pendown
tina.pensize(15)



for color in colors:
    tina.pencolor(color)
    tina.forward(50)
    tina.left(90)



# 2) Make another square, but put the colors in reverse order, using a negative index. 

... # Your code here

turtle.exitonclick()                     # Close the window when we click on it