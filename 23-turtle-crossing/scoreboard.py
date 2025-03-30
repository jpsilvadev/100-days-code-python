"""Generates and keeps track of a scoreboard for the Turtle Crossing Game!"""

from turtle import Turtle

FONT = ("Courier", 18, "bold")


class Scoreboard(Turtle):
    """Create a Scoreboard object"""

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.set_level()
        self.set_level()

    def set_level(self):
        """Set initial level count."""
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def update_level(self):
        """Update the level count."""
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def player_loss(self):
        """Print Game over."""
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", align="center", font=("Courier", 50, "bold"))
