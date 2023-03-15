#Turtle Test
#Rodrigo Takeo Miyano
#Treino
#06/03/2023

import turtle

window = turtle.Screen()
window.bgcolor("black")
window.title("Text n1")
turtle.setup(640,640)
pen = turtle.Turtle()
pen.color("white")

x,y = pen.position()
loc = str(int(x)) + "," + str(int(y))
pen.write(loc, False, align="center", font=("Arial", 24, "normal"))
pen.stamp()

pen.forward(240)
x,y = pen.position()
loc = str(int(x)) + "," + str(int(y))
pen.write(loc, False, align="center", font=("Arial", 24, "normal"))
pen.stamp()

pen.backward(480)
x,y = pen.position()
loc = str(int(x)) + "," + str(int(y))
pen.write(loc, False, align="center", font=("Arial", 24, "normal"))
pen.stamp()

pen.up
pen.goto(0,0)
pen.left(90)
pen.forward(240)
x,y = pen.position()
loc = str(int(x)) + "," + str(int(y))
pen.write(loc, False, align="center", font=("Arial", 24, "normal"))
pen.stamp()

pen.backward(480)
x,y = pen.position()
loc = str(int(x)) + "," + str(int(y))
pen.write(loc, False, align="center", font=("Arial", 24, "normal"))
pen.stamp()

pen.up
pen.left(45)
pen.forward(340.41125497)

pen.up
pen.right(90)
pen.forward(340.41125497)

pen.up
pen.right(90)
pen.forward(340.41125497)

pen.up
pen.right(90)
pen.forward(340.41125497)
