
import turtle
from turtle import *
import random

tim = Turtle()
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

directions = [0, 90, 180, 270]
tim.pensize(10)
tim.speed("fastest")

for _ in range(300):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

turtle.done()
