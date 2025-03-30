import turtle
import pandas as pd


def get_mouse_click_coor(x, y):
    print(x, y)


# setup screen with states image
screen = turtle.Screen()
screen.title("U.S. States Game")

screen.setup(width=725, height=491)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# read csv
df = pd.read_csv("50_states.csv")


# set score
score = 0

# Create lists of the states and coordinates
state_list = df.state.to_list()
x_list = df.x.to_list()
y_list = df.y.to_list()

guessed_states = []

while score < 50:
    # check answer and display state on Screen
    answer_state = screen.textinput(
        title=f"{score}/50 States", prompt="What's another state's name?"
    )
    answer_state = answer_state.title()
    if answer_state == "Exit":
        break
    if answer_state in state_list:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        index = state_list.index(answer_state)
        t.goto(x_list[index], y_list[index])
        t.write(answer_state)
        score += 1
        guessed_states.append(answer_state)
        print(guessed_states)

screen.exitonclick()

for state in guessed_states:
    if state in state_list:
        state_list.remove(state)

missing_states = pd.DataFrame(state_list)
missing_states.to_csv("missing_states.csv")
