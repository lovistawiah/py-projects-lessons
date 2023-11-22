from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
timmy.shape('triangle')
timmy.pensize(4)
timmy.penup()
timmy.left(90)
timmy.forward(90)
timmy.left(90)
timmy.forward(70)
timmy.right(90)
timmy.right(90)
timmy.pendown()


def draw_shape(num_sides, color):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.color(color)
        timmy.forward(120)
        timmy.right(angle)


for num in range(4, 12):
    colors = ["green", "yellow", "blue", "indigo", "violet", "cyan", "teal","white"]
    draw_shape(num, colors[num - 4])

screen.exitonclick()
