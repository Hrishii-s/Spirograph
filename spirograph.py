import turtle as t
import random

# spirograph
tim = t.Turtle()
tim.shape('classic')
t.colormode(255)


def randcol():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0, 255)
    clr=(r, g, b)
    return clr


tim.speed(100)
def draw(size):
    for i in range (int(360/size)):
        tim.circle(100)
        tim.setheading(tim.heading()+size)
        tim.color(randcol())

draw(5)








