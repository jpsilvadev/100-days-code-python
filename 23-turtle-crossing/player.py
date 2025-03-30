"""Template for the Player class."""

from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    "Create a new Player"

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.move_up()
        self.move_down()
        self.move_left()
        self.move_right()
        self.level_complete()
        self.go_start()

    def move_up(self):
        """move player up on key press."""
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def move_down(self):
        """move player down on key press."""
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def move_left(self):
        """move player left on key press."""
        new_x = self.xcor() - MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def move_right(self):
        """move player right on key press."""
        new_x = self.xcor() + MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def level_complete(self):
        """Check for level complete."""
        return True if self.ycor() > 280 else False

    def go_start(self):
        """Return the starting position for next level."""
        self.goto(STARTING_POSITION)
