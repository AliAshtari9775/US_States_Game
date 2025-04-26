from turtle import Turtle, Screen
import pandas


def write_state_name_on_map(pos, state_name):
    t.goto(pos)
    t.write(f"{state_name}", align='center')


# Setting up turtles to write on map
t = Turtle()
t.hideturtle()
t.penup()
t.color("black")

# Setting up the screen and background image
screen = Screen()
image = "blank_states_img.gif"
screen.addshape(image)
img = Turtle()
img.shape(image)

# Extracting Data into a pandas dataframe
data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()

# Defining a list to keep track of the correct guesses
correct_guesses_list = []

while len(correct_guesses_list) < 50:
    answer = screen.textinput(f"{len(correct_guesses_list)}/50 States Correct", "Enter State name:").title()

    # Exit program
    if answer == "Exit":
        screen.bye()
        # Generating the report CSV file
        # Finding the missing states
        missing_states_list = [state for state in states_list if state not in correct_guesses_list]

        # Creating a new pandas dataframe
        report_data = pandas.DataFrame(missing_states_list)

        # making a csv file out of that pandas dataframe
        report_data.to_csv("states_to_learn.csv")
        break

    # Checking to see if the answer is correct
    if answer in states_list:

        # Checking for duplicate answers
        if answer not in correct_guesses_list:
            # Updating the correct guessed list
            correct_guesses_list.append(answer)

            # Extracting the state data in a series
            state_data = data[data.state == answer]
            position = (state_data.x.item(), state_data.y.item())

            # Calling the dedicated function to write the name in the corresponding coordinates
            write_state_name_on_map(position, answer)
