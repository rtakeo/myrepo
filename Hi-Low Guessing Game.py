#The Hi-Low Guessing Game
#Autor: Rodrigo Takeo
#Motivo: Treinar
#Data: 24/01/23

from pcinput import getInteger
import random
from random import randint
number = random.randint(1,100)
data = "NA"
play = False
guess = -1
chances = 10

print("Welcome to the Hi-Low guessing game.")
print("I'm thinking of a number between 1 and 100")
print("You have ten attempts to guess the right number")
print("Whould you like to play the game?")
print()
data = input("yes (y/Y) or no (n/N):  ")

data = data.upper()
if data == 'y'.upper() or data == 'yes'.upper():
    while True:
        if chances <= 0:
            print("No chances left \nGame is Over")
            break
        guess = getInteger("Enter your guess 1-100 (zero to quit): ")
        if guess == 0:
            break
        elif guess > 100 or guess < 0:
            print("Numbers must be between 1 and 100 \nTry again")
            continue
        else:
            if guess > number:
                print("Guess is too high try again")
                chances -= 1
                continue
            elif guess < number:
                print("Guess is too low try again")
                chances -= 1
                continue
            elif guess == number:
                print("Correct!")
                break
        
print("...End of Program...")
