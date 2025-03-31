import random
import tkinter
import turtle
from turtle import Screen, Turtle
import math
import time

myPaddlePositionX = -200
myPaddlePositionY = -50
ballPositionX = 0
ballPositionY = -50

turtle.mode('logo')
screen = turtle.Screen()
ball = turtle.Turtle()

screen.setup(420,520)
screen.bgcolor('light blue')
ball.color('yellow')
ball.shape('circle')

ball.setpos(ballPositionX, ballPositionY)


headingEastBool = True
ballHeadingEast = random.randint(45,135)
ballHeadingWest = random.randint(225,315)
ball.seth(ballHeadingEast)
ballYCorProjection = random.randint(-6, 6)
ballXCorProjection = random.randint(-6, 6)

#gameStart()
#while ball.xcor() >= -90 and ball.xcor() <= 90:
#   gameIsOn()

#def gameStart():
#   for i in range(10):
#       ball.goto(ball.xcor()+10, ball.ycor()+ballYCorProjection)
#       time.sleep(0.5)

#def gameIsOn():
#   dwa while w forze na punkty...
#   while ball.xcor() != 90:
#


for i in range(200):
    #ball.goto(ball.xcor()+10, ball.ycor()+ballYCorProjection)
    #time.sleep(0.5)
    print('x= ', ball.xcor(), 'y= ', ball.ycor())
    if ball.xcor() <= 90 and headingEastBool == True:
        ball.goto(ball.xcor() + 10, ball.ycor() + ballYCorProjection)
        time.sleep(0.5)
        if ball.xcor() == 90:
            headingEastBool = False
    elif ball.xcor() >= -90 and headingEastBool == False:
        ball.goto(ball.xcor() - 10, ball.ycor() + ballYCorProjection)
        time.sleep(0.5)
        if ball.xcor() == -90:
            headingEastBool = True



screen.listen()
screen.exitonclick()