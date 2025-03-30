"""Generate Scoreboard for the SnakeGame"""

from turtle import Turtle


class Scoreboard(Turtle):
    """Creates a Scoreboard and updates it as the snake eats food objects"""

    def __init__(self):
        super().__init__()
        self.score = -1
        self.set_score()
        self.update_score()
        self.penup()
        self.color("white")
        self.hideturtle()

    def set_score(self):
        """Set initial scoreboard"""
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 12, "normal"))

    def update_score(self):
        """Update scoreboard as the snake eats food"""
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=("Arial", 12, "normal"))

    def game_over(self):
        """Print GameOver"""
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER!", align="center", font=("Arial", 40, "bold"))
