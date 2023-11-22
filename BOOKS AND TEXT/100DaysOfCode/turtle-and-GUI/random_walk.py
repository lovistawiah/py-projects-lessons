from turtle import Turtle,Screen
import random


timmy = Turtle()
screen = Screen()
timmy.shape("triangle")
timmy.pensize(10)
timmy.speed(5)
colors = ["green", "yellow", "blue", "indigo","violet", "cyan", "teal"]
direction = [0,90,180,270]
screen.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    return (r,g,b)
for _ in range(0,400):
    timmy.color((random_color()))
    timmy.forward(30)
    timmy.setheading(random.choice(direction))

screen.exitonclick()