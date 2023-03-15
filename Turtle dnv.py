import turtle
turtle.setup(640,640)
window = turtle.Screen()
window.bgcolor("green")
window.title("Tuple Demo")
pen = turtle.Turtle()

def goHere(x,y):
    ''' Using a tuple x.y for graphical movement.
    '''
    print(x,y)
    pen.goto(x,y)
    
x,y = pen.pos()
print(x,y)
window.onclick(goHere)
window.mainloop()