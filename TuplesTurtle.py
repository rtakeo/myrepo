# Turtle Graphics Drawing Lines - U3L2
# Purpose: To illustrate how to use functions to calculate
# Author: Rodrigo Takeo Quintella de Vasconcellos Miyano
# Date: 14/03/23

# Memory - defining libraries and enviroment setup
import turtle
from math import sqrt

turtle.setup(640,640)
window = turtle.Screen()
window.bgcolor("green")
window.title("Tuple Demo")
pen = turtle.Turtle

# Processing - Functions to calculate and report distance between two points
def distance(pA, pB):
    '''Find the distance between two points
    '''
    xsq = (pA[0] - pB[0])**2
    ysq = (pA[1] - pB[1])**2
    return sqrt(xsq + ysq)

# Input - Event driven by mouse clicks calling functions
def goHere(nx,ny):
    '''Report the distance between last point and the new point
    '''
    oldXY = pen.position()
    pen.goto(nx,ny)
    newXY = pen.position()
    lenght = distance(oldXY,newXY)
    # Output - Displaying the numerical results
    print("The distance from {},{} to {},{} is {:.2f}".format(oldXY[0],oldXY[1],newXY[0],newXY[1],lenght))

window.onclick(goHere)
window.mainloop()