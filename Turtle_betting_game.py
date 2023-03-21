from turtle import Turtle, Screen
import random as r


names = ["tim", "tom", "ton", "tot", "tel", "tek"]
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
y = -150

for x in range(6):
    names[x] = Turtle(shape="turtle")
    names[x].color(colors[x])
    names[x].up()
    y += 50
    names[x].goto(x=-240, y=y)
    all_turtles.append(names[x])

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="What turtle gonna win?", prompt="Which turtle will win the race? Enter a color: ")

if user_bet:
    is_race_on = True

while is_race_on:

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
