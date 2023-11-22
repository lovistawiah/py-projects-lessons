from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score_Board


screen = Screen()
snake = Snake()
food = Food()
score_board = Score_Board()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

screen.onkey(snake.up, key="Up")
screen.onkey(snake.down, key="Down")
screen.onkey(snake.right, key="Right")
screen.onkey(snake.left, key="Left")
game_is_on = True

while game_is_on:
    time.sleep(0.15)
    screen.update()
    snake.move()
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        score_board.keep_score()
        snake.extend_snake()

    other_snakes = snake.snake_list[1:]
    for sn in other_snakes:
        if snake.snake_head.distance(sn) < 10:
            game_is_on = False
            score_board.game_over()

    if snake.head_position.xcor() > 285 or snake.head_position.xcor() < -285 or snake.head_position.ycor() > 285 or snake.head_position.ycor() < -285:
        game_is_on = False
        score_board.game_over()


screen.exitonclick()
