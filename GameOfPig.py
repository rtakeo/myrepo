# End of UNIT 2: Programming Project - GAME OF PIG
# Purpose: Make the "Game of Pig" to train and to complete the programing project
# Author: RODRIGO TAKEO QUINTELLA DE VASCONCELLOS MIYANO
#
# Date: MARCH 12 2023
#

# Setup the initial environment
import random
import sys
import time

def printWelcome():
    # Welcome Screen 
    print("""\
           ___                       __   ___ _      
          / __|__ _ _ __  ___   ___ / _| | _ (_)__ _ 
         | (_ / _` | '  \/ -_) / _ \  _| |  _/ / _` |
          \___\__,_|_|_|_\___| \___/_|   |_| |_\__, |
                                                |___/ """)
    print("")
    print("Welcome to Game of Pig")

def printRules():
    # Human instructions
    print("")
    print("Rules of the Game:")
    print("1. Human vs. Computer - Human player against the computer")
    print("2. Game ends when one player reaches 100 banked points")
    print("3. During a turn, a player accumulates a score")
    print("   A turn ends when a player banks the score adding")
    print("   the current score to their banked score or when")
    print("   the player rolls a one [1] on the dice - loosing all")
    print("   points accumulated that round (the banked score is safe)")

def printMenu():
    # Print Menu
    print("")
    print("Menu:")
    print("(n) New Game")
    print("(r) Rules")
    print("(e) Exit")
    option = ""
    while option.lower() != "n" and option.lower() != "r" and option.lower() != "e":
        option = input("option: ")
        if option.lower() != "n" and option.lower() != "r" and option.lower() != "e":
            print("WARNING: wrong option")
    return option

def printGameover():
    # GAME OVER - Report who won 
    print("""\
             ___                   ___              
            / __|__ _ _ __  ___   / _ \__ _____ _ _ 
           | (_ / _` | '  \/ -_) | (_) \ V / -_) '_|
            \___\__,_|_|_|_\___|  \___/ \_/\___|_|  """)
    
    # Ask to Play Again
    print("Play Again?")
    
def printHumanWon():
    # HUMAN WON 
    print("""\
             _   _                       _  __  _           _  _  _
            | |_| |_ _ _ __  __ _ _ _   | |/  \| |___ _ _  | || || |
            |  _  | | | '  \/ _` | ' \  |   /\   | _ | ' \ |_||_||_|
            |_| |_|___|_|_|_\__,_|_|__\  \_/  \_/|___|_|__\[_][_][_] """)
    
    # Ask to Play Again
    print()
    print("Play Again?")

def quitGame():
    # END PROGRAM - Inform Player
    print("Thank's for playing!")
    sys.exit()
    
def printScoreboard(hs,hb,cs,cb):
    print("*******************************************")  
    print(f'* Human score:    {hs:03d}  Human bank:    {hb:03d} *')
    print(f'* Computer score: {cs:03d}  Computer bank: {cb:03d} *')
    print("*******************************************")
    
def computerOption(chaseMode,rolls):
    if chaseMode:
        if rolls < 4:
            return "r"
        else:
            return "h"
    else:
        if rolls < 3:
            return "r"
        else:
            return "h"
    
def newGame():
    # NEW GAME
    humanBank = 0
    humanScore = 0
    computerBank = 0
    computerScore = 0
    play = True
    
    # GAME LOOP
    while play == True:

        # Check game state . . Did the computer win?
        if computerBank >= 100:
            humanTurn = False
        else:
            humanTurn = True

        # a. you will need a turn loop for the human player
        # HUMAN PLAYER GOES FIRST 
        humanScore = 0     # initial value at the start of each turn
        die = 0            # impossible die value to enter player turn loop
        while humanTurn:
            print()
            print("HUMAN TURN ********************************")
            printScoreboard(humanScore, humanBank, computerScore, computerBank)
            print()
            answer = input("HUMAN: Playing (r)oll or (h)old? ")
            match answer.lower():
                case "r": # ROLL
                    # answer.lower() == 'r' and die != 1:
                    # print the roll of the die
                    die = random.randint(1,6)
                    print("HUMAN rolled \n{0}".format(dice.get(die)))
                    if die == 1:
                        # zero humanScore 
                        humanScore = 0
                        humanTurn = False
                    else:
                        # update humanScore 
                        humanScore += die
                case "h": # HOLD
                     humanTurn = False
                case _:   # WRONG OPTION
                     print("HUMAN WARNING: wrong option")
        # AFTER LOOP: update humanBank
        print("HUMAN: end of turn")
        humanBank += humanScore
        humanScore = 0
        
        # Output current state of humanScore and HumanBank to human player
        print()
        printScoreboard(humanScore, humanBank, computerScore, computerBank)
    
        # Check game state . . Did the human win?
        if humanBank >= 100:
            printHumanWon()
            play = False
            computerTurn = False
        else:
            computerTurn = True
        
        time.sleep(2)
        
        # COMPUTER PLAYER CODE HERE
        computerScore = 0  # initial value at the start of each turn
        die = 0            # impossible die value to enter player turn loop
        # a. you will need a turn loop for the human player
        # check if computer is chasing human or not
        if computerTurn and (computerBank+10 < humanBank or computerBank >= 75):
            #    The computer needs to 'chase' the human if behind in points.
            #    The computer needs to 'risk' more if close to the goal of 100 points
            chaseMode = True
            print("ATTENTION: COMPUTER is chasing")            
        else:
            #    The computer needs to play conservatively if it is winning
            chaseMode = False
        rolls = 0
        # a. Inteligent turn loop for computer .. think about it .. code it.
        while computerTurn:
            print()
            print("COMPUTER TURN *****************************")
            printScoreboard(humanScore, humanBank, computerScore, computerBank)
            print()
            # first level intelligence
            answer = computerOption(chaseMode,rolls)
            if computerBank + computerScore >= 100:
                answer = "h"
            match answer.lower():
                case "r": # ROLL
                    die = random.randint(1,6)
                    print("COMPUTER rolled \n{0}".format(dice.get(die)))
                    if die == 1:
                        # zero humanScore 
                        computerScore = 0
                        computerTurn = False
                    else:
                        # update humanScore 
                        computerScore += die
                case "h": # HOLD
                     computerTurn = False
                case _:   # WRONG OPTION
                     print("COMPUTER WARNING: wrong option")
            rolls += 1
            time.sleep(2)
            
        # AFTER LOOP: update computerBank
        print("COMPUTER: end of turn")
        computerBank += computerScore
        computerScore = 0
    
        # Check game state . . Did the computer win?
        if computerBank >= 100:
            printGameover()
            play = False
            humanTurn = False
        else:
            humanTurn = True
            
    # Check Game State ... if 
    

# Data structures
# a dictionary of dice - a data structure to make the game pretty
dice = { 1 : "+-------+     --------    \n"+
             "|       |    / []  [] \   \n"+
             "|   o   |    |   /\   |   \n"+
             "|       |    \_      _/   \n"+
             "+-------+      UUUUUU     ",
         2 : "+-------+\n"+
             "| o     |\n"+
             "|       |\n"+
             "|     o |\n"+
             "+-------+",
         3 : "+-------+\n"+
             "| o     |\n"+
             "|   o   |\n"+
             "|     o |\n"+
             "+-------+",
         4 : "+-------+\n"+
             "| o   o |\n"+
             "|       |\n"+
             "| o   o |\n"+
             "+-------+",
         5 : "+-------+\n"+
             "| o   o |\n"+
             "|   o   |\n"+
             "| o   o |\n"+
             "+-------+",
         6 : "+-------+\n"+
             "| o   o |\n"+
             "| o   o |\n"+
             "| o   o |\n"+
             "+-------+",
         }


# BEGIN
printWelcome()
printRules()
option = ""
while True:
    option = printMenu()
    match option:
        case "r":
             printRules()
        case "e":
             quitGame()
        case "n":
             newGame()



    