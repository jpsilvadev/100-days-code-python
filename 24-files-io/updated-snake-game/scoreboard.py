"""Generate Scoreboard for the SnakeGame"""

from turtle import Turtle


class Scoreboard(Turtle):
    """Creates a Scoreboard and updates it as the snake eats food objects"""

    def __init__(self):
        super().__init__()
        self.score = -1
        with open("data.txt") as data:
            self.high_score = int(data.read())
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
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            align="center",
            font=("Arial", 12, "normal"),
        )

    def reset(self):
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     """Print GameOver"""
    #     self.goto(0, 0)
    #     self.color("red")
    #     self.write("GAME OVER!", align="center", font=("Arial", 40, "bold"))
