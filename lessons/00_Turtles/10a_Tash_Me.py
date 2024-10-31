""" Tash Me

Write a program that:
1) Loads an emoji image as the background
2) Make the turtle shape a moustach
3) Move the moustache to the right spont on the emoji

Hint: See 08a_More Turtle Programs, section 'Change the Background Image' and
'Change the Turtle Shape'
"""

... # Your code here

import turtle 

def set_background_image(window, image_name):
    
    from pathlib import Path
    from PIL import Image

    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    image = Image.open(image_path)


    window.setup(image.width, image.height, startx=0, starty=0)
    window.bgpic(image_path)


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





t = turtle.Turtle()

sti(t, "moustache1.gif")
t.penup()
t.speed(3)

for i in range(4):
    tina.goto(200, 200)
    tina.goto(-200, -200)


turtle.setup(width=600, height=600)
set_background_image(screen, "emoji.png")
turtle.exitonclick()
