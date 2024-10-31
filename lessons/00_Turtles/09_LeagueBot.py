""" Leaguebot

Write your own turtle program! Here is what your program should do

1) Change the turtle image to 'leaguebot_bolt.gif'
2) Change the turtle size to 10x10
3) Change the turtle line color to 'blue'
4) Draw a hexagon using a loop and variables. 

"""

import turtle as turtle
import turtle
turtle.setup(width=600, height=600)



TsCode = turtle.Turtle()


TsCode.turtlesize(stretch_wid=10, stretch_len=10, outline=0)

TsCode.goto(0,0)


def sti(turtle, turtle_image_name):

    from pathlib import Path

    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / turtle_image_name)


    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)


sti(TsCode, "leaguebot_bolt.gif")


TsCode.penup()
TsCode.pendown()

TsCode.pencolor('blue')

TsCode.speed(1)

for i in range(6):
    TsCode.forward(150)
    TsCode.left(60)

TsCode.penup()


turtle.exitonclick()