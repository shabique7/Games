from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(x=-100,y=200)
        self.write(self.l_score,align="Center",font=("Courier",50,"normal"))
        self.goto(x=100, y=200)
        self.write(self.r_score, align="Center", font=("Courier", 50, "normal"))

    def l_point(self):
        self.l_score +=1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()