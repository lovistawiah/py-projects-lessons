from turtle import Screen
import time
from ball import Ball
from player import Player
from pitch import Pitch
from scoreboard import Score_board


screen = Screen()
screen.tracer(0)
screen.title("Pong")

pong_player_1 = Player(350, 0)
pong_player_2 = Player(-350, 0)
ball = Ball()
pitch = Pitch()
score_board = Score_board()


screen.setup(width=900, height=600)
screen.bgcolor("black")
screen.listen()
screen.onkey(pong_player_1.Up, key="Up")
screen.onkey(pong_player_1.Down, key="Down")
screen.onkey(pong_player_2.Up, key="w")
screen.onkey(pong_player_2.Down, key="s")

game_is_on = True


while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # Detect collision with right paddle
    if ball.distance(pong_player_1) and ball.xcor() < 340:
        ball.x_bounce()

screen.exitonclick()
