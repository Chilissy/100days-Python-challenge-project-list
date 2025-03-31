import random
import tkinter
import turtle
from turtle import Screen, Turtle
import keyboard
import time

myPaddlePositionX = -200
myPaddlePositionY = -50
ballPositionX = 0
ballPositionY = -50

turtle.mode('logo')
screen = turtle.Screen()
ball = turtle.Turtle()
myPaddle = turtle.Turtle()
ball.penup()
myPaddle.penup()

screen.setup(420,520)
screen.bgcolor('light blue')
ball.color('yellow')
ball.shape('circle')
myPaddle.shape("square")
myPaddle.color("dark red")

myPaddle.setpos(myPaddlePositionX, myPaddlePositionY)
ball.setpos(ballPositionX, ballPositionY)

def ballRebounce():
    ballHeading = random.randint(225, 315)
    ball.seth(ballHeading)
    for i in range(200):
        ball.fd(10)
        time.sleep(0.5)
        if ball.xcor() == -90:
            ballBounce()
        elif ball.xcor() == -100:
            print('game over')
            exit()

def ballBounce():
    ballHeading = random.randint(45,135)
    ball.seth(ballHeading)
    for i in range(200):
        ball.fd(10)
        time.sleep(0.5)
        if ball.xcor() == 90:
            ballRebounce()
            print('okopkok')
        elif ball.xcor() == 100:
            print('game over')
            exit()


ballBounce()
ballRebounce()

def moveUp():
    myPaddle.seth(0)
    myPaddle.fd(10)

screen.onkey(moveUp, 'w')



screen.listen()
screen.exitonclick()