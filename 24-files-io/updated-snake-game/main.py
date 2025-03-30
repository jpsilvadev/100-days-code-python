"""SnakeGame"""

from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# setup canvas and background
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SnakeGame")
screen.tracer(0)

# create snake --> 3 white blocks 20x20
snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

PLAY_SNAKE = True
while PLAY_SNAKE:
    screen.update()
    time.sleep(0.1)

    # move snake
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.update_score()

    # detect collision with wall
    if (
        snake.head.xcor() > 290
        or snake.head.xcor() < -290
        or snake.head.ycor() > 290
        or snake.head.ycor() < -290
    ):
        score.reset()
        snake.reset()

    # detect collision with snake segments
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            score.reset()

screen.exitonclick()
