from turtle import Turtle


class Score_Board(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.ALIGNMENT = "center"
        self.FONT = ("Arial", 24, "normal")
        self.write_to_screen()
        self.hideturtle()

    def keep_score(self):
        self.clear()
        self.score += 1
        self.write_to_screen()

    def write_to_screen(self):
        self.write(f"Score: {self.score}",align=self.ALIGNMENT, font=self.FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!",align=self.ALIGNMENT, font=self.FONT)
