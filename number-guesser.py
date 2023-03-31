#Number Guessing Game Objectives:
import random


random_nr = random.randint(0,100)
easy = 10
hard = 5


""" check() method contains the user_input variable and changes it to int. It also contains number() method with status parameter. 
number() method compares the user_input with randomly generated number and returns the status of the equation."""

def check():
    user_input = input("What number?")
    user_input = int(user_input)
    def number(status):
        if user_input == random_nr:
            print("Great!")
            quit()
        elif user_input < random_nr:
            status = "Too low"
            return status
        else:
            status = "Too high"
            return status
    print(number(user_input))
    
    
""" Code below allow player to choose the difficulty. Playing on hard difficulty gives player 5 chances to guess the correct number and easy 10."""

z = input("Hey, let's play guess the number game. Do you want the difficulty to be easy or hard?")

if z == "easy":
    for i in range (0, easy):
        check()
else:
    for i in range (0, hard):
        check()
