from turtle import Turtle, Screen
import random as r


names = ["tim", "tom", "ton", "tot", "tel", "tek"]
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
y = -150


""" BELOW: This loop creates the Turtle object with shape=turtle, colors it and use goto() function to setup the turtle starting position."""
for x in range(6):
    names[x] = Turtle(shape="turtle")
    names[x].color(colors[x])
    names[x].up()
    y += 50
    names[x].goto(x=-240, y=y)
    all_turtles.append(names[x])

    
""" BELOW: This code creates Screen object, set up its size and creates the user_bet variable that opens up a window with prompt. The prompt input is
        later saved in that variable."""
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="What turtle gonna win?", prompt="Which turtle will win the race? Enter a color: ")

""" BELOW: Checks if user_bet == True (if there's any input), if so, then it continue with while loop."""
if user_bet:
    is_race_on = True

while is_race_on:

    """ BELOW: Distance variable is a random integer. turtle.forward makes turtle go forward by the 'distance' variable. Next, if 'x colored' turtle passes the
            x coordinate which is equal to 250, then that 'x colored' turtle win. Then 'if' statements checks, if user_bet == the color of the turtle that won."""
    for turtle in all_turtles:
        distance = r.randint(0, 10)
        turtle.forward(distance)
        if turtle.xcor() >= 250:
            print(f"Turtle {turtle.pencolor()} won")
            if user_bet == turtle.pencolor():
                print("You won!")
                quit()
            else:
                print("You lost!")
                quit()

screen.exitonclick()
