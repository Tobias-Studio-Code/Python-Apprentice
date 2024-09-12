"""

Copy the code from the previous lesson, 08a_More_Turtle_programs.ipynb, 
from the section "Change the Background Image"


Then change the code so that the turtle has a different image ( look in the 'images'
directory ) and moves to the corners of the screen in a square pattern. 
"""
"""

"""

import turtle 

def set_background_image(window, image_name):
    
    from pathlib import Path
    from PIL import Image

    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    image = Image.open(image_path)


    window.setup(image.width, image.height, startx=0, starty=0)
    window.bgpic(image_path)


turtle.setup(width=600, height=600)
tina = turtle.Turtle()

screen = turtle.Screen()
set_background_image(screen, "emoji.png")





def sti(turtle, turtle_image_name):
    
    from pathlib import Path


    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / turtle_image_name)

    

    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)




screen = turtle.Screen()
screen.setup(width=600, height=600)

t = turtle.Turtle()

sti(t, "emoji2.png")
t.penup()
t.speed(3)

for i in range(4):
    tina.goto(200, 200)
    tina.goto(-200, -200)


set_background_image(screen, "emoji2.png")
turtle.exitonclick()