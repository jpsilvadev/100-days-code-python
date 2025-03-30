"""Generate Ball Class"""

from turtle import Turtle


class Ball(Turtle):
    """Ball object template class"""

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.x_move = 15
        self.y_move = 15
        self.move_speed = 0.1

    def move(self):
        """move the ball"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """bounce the ball from top/bottom wall"""
        self.y_move *= -1

    def bounce_x(self):
        """bounce the ball from the paddle on contact"""
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """reset the game"""
        self.goto(0, 0)
        self.move_speed = 0.1
        self.x_move *= -1
