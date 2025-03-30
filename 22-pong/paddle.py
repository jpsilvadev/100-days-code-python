"""Generate Paddle Class"""

from turtle import Turtle


class Paddle(Turtle):
    """Paddle object template class"""

    def __init__(self, position):
        super().__init__()
        self.position = position
        self.color("white")
        self.shape("square")
        self.penup()
        self.speed("fastest")
        self.goto(position)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.move_down()
        self.move_up()

    def move_up(self):
        """Move up"""
        new_y = self.ycor() + 30
        self.goto(x=self.xcor(), y=new_y)

    def move_down(self):
        """Move down"""
        new_y = self.ycor() - 30
        self.goto(x=self.xcor(), y=new_y)
