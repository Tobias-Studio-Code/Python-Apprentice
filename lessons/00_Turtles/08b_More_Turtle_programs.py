"""

Copy the code from the previous lesson, 08a_More_Turtle_programs.ipynb, 
from the section "Change the Turtle Image"


Then change the code so that the turtle has a different image ( look in the 'images'
directory ) and moves to the corners of the screen in a square pattern. 
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

import turtle
turtle.setup(width=600, height=600)
tina = turtle.Turtle()

screen = turtle.Screen()
set_background_image(screen, "emoji.png")
turtle.exitonclick()