from random import *
from turtle import *



t=Turtle()

def drawRect(W,H,Color):
    
    
    t.color(Color)
    t.begin_fill()



    for i in range(4):
        t.forward(W)

        t.left(90)

        t.forward(H)
        t.left(90)

    t.end_fill()



drawRect(35,15,"Green")        





update()
mainloop()
   
    

