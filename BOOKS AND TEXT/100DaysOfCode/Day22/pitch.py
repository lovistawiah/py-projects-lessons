from turtle import Turtle


class Pitch(Turtle):
    def __init__(self):
        self.create_pitch()

    def create_pitch(self):
        self.starting_position = -270
        for _ in range(12):
            self.pitch = Turtle("square")
            self.pitch.penup()
            self.pitch.color("blue")
            self.pitch.goto(0,self.starting_position)
            self.pitch.shapesize(1, 0.3, 2)
            self.starting_position += 50
