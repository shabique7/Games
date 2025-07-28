from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len = 1, stretch_wid = 1)
        self.speed("fastest")
        random_x = random.randint(-200,200)
        random_y = random.randint(-200, 200)
        self.goto(random_x,random_y)
        self.refresh()
        self.change_color()

    def change_color(self):
        colors = [ "red","orange","yellow","lime","cyan","deepskyblue","blue","magenta","hotpink","deeppink","white"]
        self.color(random.choice(colors))

    def refresh(self):
        random_x = random.randint(-200, 200)
        random_y = random.randint(-200, 200)
        self.goto(random_x, random_y)