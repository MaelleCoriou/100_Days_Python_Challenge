import turtle
import pandas as pd
from game import find_state, show_state

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed = []
missed_states = []

screen = turtle.Screen()
screen.title(f"U.S. State Game")
# Use the image as turtle shape
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Turtle for input answer
answer = turtle.Turtle()
answer.hideturtle()
answer.penup()

# Turtle to show all states
correction = turtle.Turtle()
correction.color("red")
correction.hideturtle()
correction.penup()

while len(guessed) < 50:
    answer_state = screen.textinput(title=f"{len(guessed)}/50 states correct",
                                    prompt="What's another state's name?").title()

    if find_state(data, answer_state, answer):
        guessed.append(answer_state)

        # If the state is entered twice, guessed list updated to avoid duplicated states
        if answer_state in guessed:
            count = guessed.count(answer_state)
            if count > 1:
                guessed.remove(answer_state)

    # enter exit to get the list of the states to learn
    elif answer_state == "Exit":
        for states in all_states:
            if states not in guessed:
                missed_states.append(states)
        missed_states = pd.DataFrame(missed_states)
        missed_states.to_csv("not_found_states.csv")
        break

    # If the answer isn't in the list, the game stops
    else:
        # Shows all states on the map when game is over
        show_state(data, missed_states, correction)
        break

correction.clear()
turtle.write(f"Final score {len(guessed)}/50", font="50", align="center")
turtle.mainloop()

# function to get the mouse coordinates when clicking on the map
# won't be used as coordinates are recorded in csv file already :

# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
