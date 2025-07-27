import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
tim.pensize(7)

colors = ["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","wheat","Slategray","SeaGreen"]

def draw_shape(num_sides):
    for _ in range(num_sides):
        angle = 360 / num_sides
        tim.forward(100)
        tim.right(angle)

for shape_side in range(3,15):
    tim.color(random.choice(colors))
    draw_shape(shape_side)


screen = Screen()
screen.exitonclick()