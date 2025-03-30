"""Pong Arcade Game"""

from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


# Create screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Create and move right paddle
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()


screen.listen()

screen.onkey(key="Up", fun=r_paddle.move_up)
screen.onkey(key="Down", fun=r_paddle.move_down)
screen.onkey(key="w", fun=l_paddle.move_up)
screen.onkey(key="s", fun=l_paddle.move_down)

PLAY_PONG = True
while PLAY_PONG:
    time.sleep(ball.move_speed)
    screen.update()

    ball.move()

    # detect collision with top and bottom wall --> 800 x 600
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with right paddle --> Draw line on x-axis as limit
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    elif ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect if ball goes off screen and add score
    elif ball.xcor() > 390:
        ball.reset_position()
        score.l_point()
    elif ball.xcor() < -390:
        ball.reset_position()
        score.r_point()


screen.exitonclick()
