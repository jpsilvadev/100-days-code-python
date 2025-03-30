"""Creates a food object for the SnakeGame"""

from turtle import Turtle
import random


class Food(Turtle):
    """Creates a food object for the snake to eat

    Parameters
    ----------
    Turtle : SuperClass from the turtle module
    """

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Generate new food object after it is eaten by the snake"""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
