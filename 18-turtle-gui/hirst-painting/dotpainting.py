import colorgram
from turtle import Turtle, Screen, colormode
import random

rgb_colors = []
colors = colorgram.extract("image.jpg", 30)
for color in colors:
    rgb_colors.append(tuple(color.rgb))

print(rgb_colors)

t = Turtle()
colormode(255)
t.speed("fastest")
t.penup()
t.hideturtle()

for y in range(-350, 400, 50):
    for x in range(-400, 400, 50):
        t.goto(x, y)
        t.dot(20, random.choice(rgb_colors))

screen = Screen()
screen.exitonclick()
