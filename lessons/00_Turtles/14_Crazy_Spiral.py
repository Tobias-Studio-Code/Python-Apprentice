"""
Crazy Spiral

Make your own crazy spiral with a pattern like
in 14_FLaming_Ninja_Star.py, but use what you've learned about loops
"""

... # Copy code to make a turtle and set up the window
import turtle
import turtle as turtle
turtle.setup(width=600,height=600)
TsCode = turtle.Turtle()
import random


# 1) Complete make_a_shape() to make the turtle move in some pattern. 
# For instance, you can make it go left 30 degrees, then forward 50 pixels, 
# then right 60 degrees, then forward 100 pixels. Make any shape you like.


# 2) Call make_a_shape() in a loop to make the turtle draw a spiral.
# For instance, you can call make_a_shape() 100 times to make a spiral with 100 shapes.
# The second ... in the for loop should be the number of shapes you want to make, 

TsCode.speed(10)
num_shapes = 60
TsCode.penup


for i in range(35):

    TsCode.forward(20) 

    TsCode.speed(1)

    TsCode.left(200) 

    TsCode.forward(20) 

    TsCode.right(170) 

    TsCode.forward(20) 

    TsCode.right(40) 

    TsCode.forward(20) 

    TsCode.speed(5)

    TsCode.tilt(360)

turtle.exitonclick()