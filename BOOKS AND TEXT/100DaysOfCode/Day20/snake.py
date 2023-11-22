from turtle import Turtle


class Snake(Turtle):
    def __init__(self) -> None:
        self.snake_list = []
        self.xcor = 0.0
        self.move_distance = 20
        self.xposition = 0.00
        self.create_snake()
        self.snake_head = self.snake_list[0]
        self.LEFT = 180
        self.RIGHT = 0
        self.UP = 90
        self.DOWN = 270
        self.head_position = self.snake_head
        self.snake_length = len(self.snake_list)

    def create_snake(self):
        for _ in range(3):
            snake = Turtle("square")
            snake.color("white")
            snake.penup()
            self.xposition = snake.xcor()
            snake.setx(self.xcor)
            self.xcor -= 20
            self.snake_list.append(snake)

    def extend_snake(self):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        self.xposition = self.snake_list[self.snake_length - 1].xcor() - 20
        snake.setx(self.xposition)
        self.snake_list.append(snake)

    def move(self):
        for snake_num in range(len(self.snake_list)-1, 0, -1):
            new_x = self.snake_list[snake_num-1].xcor()
            new_y = self.snake_list[snake_num-1].ycor()
            self.snake_list[snake_num].goto(new_x, new_y)
        self.snake_list[0].forward(self.move_distance)

    def up(self):
        if self.snake_head.heading() != self.DOWN:
            self.snake_head.setheading(self.UP)

    def down(self):
        if self.snake_head.heading() != self.UP:
            self.snake_head.setheading(self.DOWN)

    def right(self):
        if self.snake_head.heading() != self.LEFT:
            self.snake_head.setheading(self.RIGHT)

    def left(self):
        if self.snake_head.heading() != self.RIGHT:
            self.snake_head.setheading(self.LEFT)
