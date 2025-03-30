from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def move_clockwise():
    heading = tim.heading()
    tim.setheading(heading - 15)


def move_counterclockwise():
    heading = tim.heading()
    tim.setheading(heading + 15)


def clear_screen():
    tim.home()
    tim.clear()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="a", fun=move_counterclockwise)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
