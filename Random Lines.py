import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
t.colormode(255)
tim.pensize(7)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

directions = [0,90,180,360]
tim.pensize(10)
tim.speed("fast")

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()