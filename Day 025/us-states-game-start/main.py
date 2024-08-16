import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

score = 0
game_complete = False
states = pandas.read_csv("50_states.csv")
all_states = states.state.to_list()
correct_answers = []

while not game_complete:
    answer_state = (screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state name?")).title()

    # Check if answer is already guessed
    if answer_state in correct_answers:
        continue
    # Exit game
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in correct_answers:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    check_answer_correct = states[states.state == answer_state]
    if check_answer_correct.empty:
        continue
    else:
        answer_correct_x = check_answer_correct.x
        answer_correct_y = check_answer_correct.y

        pen = turtle.Turtle()
        pen.hideturtle()
        pen.penup()
        pen.goto(int(answer_correct_x.values[0]), int(answer_correct_y.values[0]))
        pen.write(answer_state, align="center", font=("Arial", 7, "bold"))
        correct_answers.append(answer_state)
        score += 1

# states to learn.csv
