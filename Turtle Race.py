from turtle import Turtle, Screen
import random
import tkinter.messagebox as messagebox
screen = Screen()
screen.setup(height=400,width=500)
colors = ["red","orange","yellow","green","blue","purple"]
user_bet = screen.textinput(title="Make your bet",prompt="Which Turtle Will Win The Race?Enter a color: ").lower()
all_turtle = []

y_position = [-70, -40, -10, 20, 50, 80]
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 225:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                messagebox.showinfo("Race Result" ,f"You've WON !! The {winning_color} turtle is the winner!")
            else:
                messagebox.showinfo("Race Result" ,f"You've LOST !! The {winning_color} turtle is the winner!")
            break
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
screen.exitonclick()