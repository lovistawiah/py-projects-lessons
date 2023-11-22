from turtle import Turtle, Screen
import random

colors = ["red", "green", "yellow", "blue", "violet", "indigo", "black"]
turtles = []
for name in range(6):
    t = Turtle(shape="turtle")
    t.color(colors[name])
    turtles.append(t)


screen = Screen()
screen.setup(width=500, height=400)

y_cord = -170
x_cord = -230
for turtle in turtles:
    turtle.penup()
    turtle.goto(x=x_cord, y=y_cord)
    y_cord += 50

bet = screen.textinput("Make a bet","Enter your choice of color: ")
final_point = 230
start_point = x_cord
is_finished = True
while is_finished:
    for turtle in turtles:
        rand = random.randint(1, 5)
        turtle.forward(rand)
        if turtle.xcor() >= final_point:
            winner = turtle.color()[0]
            is_finished = False
            if bet == winner:
                print("congrats! You win")
            else:
                print("You lose")

screen.exitonclick()
