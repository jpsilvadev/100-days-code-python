"""Race a bunch of turtles!"""

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which turtle will win the race?\
 Enter a color:",
)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y_positions = [-70, -40, -10, 20, 50, 80]

all_turtles = []
for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

IS_RACE_ON = False

if user_bet:
    IS_RACE_ON = True

while IS_RACE_ON:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            IS_RACE_ON = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")

        distance = random.randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()
