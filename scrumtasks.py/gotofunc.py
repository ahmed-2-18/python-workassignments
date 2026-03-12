from random import *
from turtle import *



t=Turtle()

def goToRandom(centerX,centerY,W,H):
    t.penup()
    
    #  x bounds
    X = centerX -W/2
    X2 = centerX + W/2

    # y bounds
    Y = centerY - H/2
    Y2= centerY + H/2


    randomX = randint(X,X2)

    randomY = randint(Y,Y2)


    t.goto(randomX,randomY)
    t.pendown()




    

