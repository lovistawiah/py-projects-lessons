from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def turn_right():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def turn_left():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="a", fun=turn_right)
screen.onkey(key="f", fun=turn_left)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
