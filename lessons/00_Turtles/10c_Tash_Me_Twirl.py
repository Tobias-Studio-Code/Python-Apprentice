
""" Tash Me with a Twirl
 
Update your Tash Me Click program ( copy your old program here )
so the moustache will twirl when you click on it. 

Hint: See 08a_More Turtle Programs, section 'Click on the Turtle'
"""

#yup gottit

import turtle 
turtle.setup(width=600, height=600)
def set_background_image(window, image_name):
    
    from pathlib import Path
    from PIL import Image

    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    image = Image.open(image_path)


    window.setup(image.width, image.height, startx=0, starty=0)
    window.bgpic(image_path)






screen = turtle.Screen()






def sti(turtle, turtle_image_name):
    
    from pathlib import Path


    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / turtle_image_name)

    

    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)





t = turtle.Turtle()
t.turtlesize(stretch_wid=10, stretch_len=10, outline=4)
sti(t, "moustache1.gif")
t.penup()
t.speed(1)



set_background_image(screen, "emoji.png")
t.shape("turtle")

def screen_clicked(x,y):
    print(str(x)+str(y))

    t.goto(x,y)


def turtle_clicked(t,x,y):


    for i in range(0, 360, 20):
        t.tilt(20)
        print("^")
     
t.onclick(lambda x,y,t=t: turtle_clicked(t,x,y))

screen.onclick(screen_clicked)

turtle.done()