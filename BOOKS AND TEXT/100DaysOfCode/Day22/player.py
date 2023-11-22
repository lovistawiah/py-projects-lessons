from turtle import Turtle


class Player(Turtle):
    def __init__(self, x_starting_position, y_starting_position):
        """
        ***This creates player(s) by inserting***
        eg: x_starting_position = 350,y_starting_position = 30
        """
        self.y_starting_position = y_starting_position
        self. x_starting_position = x_starting_position
        self.create_squares()
        self.y_position = self.square.ycor()

    def create_squares(self) -> None:
        self.square = Turtle("square")
        self.square.penup()
        self.square.color("white")
        self.square.setx(self.x_starting_position)
        self.square.sety(self.y_starting_position)
        self.square.shapesize(stretch_wid=5, stretch_len=1)

    def Up(self):
        if self.square.ycor() <= 240:
            self.y_position += 30
            self.square.goto(self.square.xcor(), self.y_position)

    def Down(self):
        if self.square.ycor() >= -235:
            self.y_position -= 30
            self.square.goto(self.square.xcor(), self.y_position)
