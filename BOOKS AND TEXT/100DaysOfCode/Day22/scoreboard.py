from turtle import Turtle


class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.first_player = 0
        self.second_player = 0
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.write_score(self.first_player, self.second_player)

    def write_score(self, first_player, second_player):
        """
        with condition,
        increase a player's score when scores
        """
        self.clear()
        self.write(f"{first_player}  :  {second_player}",
                   align="center", font=("Courier", 20, "normal"))
