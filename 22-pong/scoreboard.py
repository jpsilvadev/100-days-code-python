"""Create a scoreboard for the Pong Game"""

from turtle import Turtle


class Scoreboard(Turtle):
    """Keeps track of the scoreboard"""

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update_score()

    def update_score(self):
        """Update the scoreboard on the screen"""
        self.clear()
        self.goto(-150, 220)
        self.write(self.l_score, align="center", font=("Arial", 50, "bold"))
        self.goto(150, 220)
        self.write(self.r_score, align="center", font=("Arial", 50, "bold"))

    def l_point(self):
        """Update scoreboard with left point"""
        self.l_score += 1
        self.update_score()

    def r_point(self):
        """Update scoreboard with right point"""
        self.r_score += 1
        self.update_score()
