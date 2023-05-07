import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. STATES QUIZ")
IMAGE = "blank_states_img.gif"
guessed_states = []
screen.addshape(IMAGE)
turtle.shape(IMAGE)

game_is_on = True
data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()

while game_is_on:
    answer_state = screen.textinput(title=f"Guess state {len(guessed_states)}/50",
                                    prompt="Please input your state name")
    if answer_state:
        write_turtle = turtle.Turtle()
        write_turtle.hideturtle()
        title_case = answer_state.title()
        if title_case in states_list:
            required_state = data[data.state == title_case]
            write_turtle.penup()
            write_turtle.goto(int(required_state.x), int(required_state.y))
            write_turtle.write(f"{title_case}", align="center", font=('Arial', 14, 'normal'))
            guessed_states.append(title_case)
            if len(guessed_states) == 50:
                game_is_on = False
    else:
        game_is_on = False

states_to_learn = [item for item in states_list if item not in guessed_states]

df = pandas.DataFrame(states_to_learn)
df.to_csv("learning.csv")
