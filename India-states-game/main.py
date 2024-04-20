import turtle
import pandas as pd

data = pd.read_csv("states_data.csv")
states = data["state"].to_list()

screen = turtle.Screen()
screen.title("India States Game")
image = "India-state.gif"
screen.addshape(image)
turtle.shape(image)

guessed_states = []

while len(guessed_states) < 30:
    answer = screen.textinput(title=f"{len(guessed_states)}/30 States Correct", prompt="What's the next state?").title()
    if answer == "Exit":
        missing_states = []
        for state in states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learns.csv")
        break
    if answer in states:
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["state"] == answer]
        t.goto(int(state_data["x"]), int(state_data["y"]))
        t.write(answer)

