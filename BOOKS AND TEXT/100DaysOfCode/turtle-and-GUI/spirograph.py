from turtle import Turtle, Screen
import random
tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.pensize(2)
tim.speed("fast")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


for i in range(int(360/ 10)):
    tim.circle(100, 360)
    tim.pencolor(random_color())
    current_heading = tim.heading()
    tim.setheading(current_heading + 10)


screen.exitonclick()
