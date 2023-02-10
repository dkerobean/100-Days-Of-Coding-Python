from turtle import Turtle, Screen
import pandas

turtle = Turtle()
screen = Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")

guessed_states = []

while len(guessed_states) < 50:
    user_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct", prompt="What is another state").title()
    all_states = data["state"].to_list()

    if user_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        break

    if user_state in all_states:
        guessed_states.append(user_state)
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["state"] == user_state]
        t.goto(int(state_data["x"]), int(state_data["y"]))
        t.write(user_state)


















screen.exitonclick()








