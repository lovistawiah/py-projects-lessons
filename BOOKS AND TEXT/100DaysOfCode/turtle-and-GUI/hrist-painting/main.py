import random
from turtle import Turtle, Screen

t = Turtle()
s = Screen()
s.colormode(255)
color_palette = [(236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216), (217, 163, 101), (27, 105, 168), (35, 186, 109), (19, 29, 168), (13, 23, 66), (212, 135, 177), (233,
                                                                                                                                                                                                               223, 7), (199, 33, 132), (13, 183, 212), (230, 166, 199), (126, 189, 162), (8, 49, 28), (40, 132, 77), (128, 219, 232), (58, 12, 25), (67, 22, 7), (114, 90, 210), (146, 216, 199), (179, 17, 8), (233, 66, 34)]


def random_color():
    return random.choice(color_palette)



def dot_and_position(num_dot):
    x_change_position = 50
    y_change_position = 40
    x = -270
    y = -200

    for dot_count in range(num_dot):
        t.hideturtle()
        t.penup()

        if dot_count % 10 == 0:
            y += y_change_position
            x = -270

        t.goto(x,y)
        t.showturtle()
        t.pendown()
        t.dot(20, random_color())
        x += x_change_position
    
    t.hideturtle()

dot_and_position(100)
s.exitonclick()
