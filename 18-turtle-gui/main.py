from turtle import Turtle, Screen, pen
import random

MAX_ANGLE = 360

tim = Turtle()
### Challenge 2
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


### Challenge 3

# colors = ["DeepSkyBlue", "DarkOrange3", "cyan", "aquamarine", "chartreuse", "coral", "magenta", "NavyBlue"]

# def draw_shape(num_sides):
#     for _ in range(num_sides):
#         tim.color()
#         tim.forward(100)
#         tim.right(MAX_ANGLE/num_sides)


# for i in range(3,11):
#     tim.color(choice(colors))
#     draw_shape(i)


### Challenge 4

# colors = ["DeepSkyBlue", "DarkOrange3", "cyan", "aquamarine", "chartreuse", "coral", "magenta", "NavyBlue"]
# direction = [0,90,180,270]

# screen = Screen()
# screen.colormode(255)
# tim.pensize(15)
# tim.speed("fastest")
# for _ in range(500):
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     tup = (r,g,b)
#     tim.pencolor(tup)
#     tim.forward(30)
#     tim.setheading(random.choice(direction))


# screen.exitonclick()


### Challenge 5


screen = Screen()
screen.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


tim.speed("fastest")


def draw_spirograph(size_gap):
    for _ in range(360 / size_gap):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_gap)


draw_spirograph(5)

screen.exitonclick()
