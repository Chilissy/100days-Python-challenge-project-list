#Number Guessing Game Objectives:
import random
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

RANDOM_NUMBER = random.randint(0,100)
EASY = 10
HARD = 5

def check():
    user_input = input("What numbah?")
    user_input = int(user_input)
    def number(status):
        if user_input == RANDOM_NUMBER:
            print("Great!")
            quit()
        elif user_input < RANDOM_NUMBER:
            status = "Too low"
            return status
        else:
            status = "Too high"
            return status
    print(number(user_input))

z = input("Hey, let's play guess the number game. Do you want the difficulty to be easy or hard?")

if z == "easy":
    for i in range (0, EASY):
        check()
else:
    for i in range (0, HARD):
        check()
