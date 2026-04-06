from turtle import *
from random import *


t = Turtle()

def drawPizza():
    tracer(0)

    t.speed(10)
    t.penup()
    
    t.right(90)
    t.forward(100)
    t.setheading(0)
    t.pendown()
    t.color("#8A6500")
    t.begin_fill()
    t.circle(100)
    t.end_fill()
   
    t.penup()
    #t.goto(0, -85)
    t.left(90)
    t.forward(15)
    t.setheading(0)
    t.pendown()
    t.color("orange")
    
    #color of inner circle
    t.begin_fill()

    t.circle(85)
    t.end_fill()

    #slices
    t.color("black")
    
    t.left(90)
    t.forward(85)
    for i in range(8):
        t.pendown()
        t.forward(85)
        t.penup()
        t.left(180)
        t.forward(85)
        t.left(45)

def drawStickMan():
    tracer(0)
    t.pendown()
    t.setheading(0)
    t.speed(10)
    


    t.circle(30)

   

    t.pendown()
    t.setheading(270) 
    t.forward(100)


    t.left(45)
    t.forward(50)
    t.backward(50)

# left leg
    t.right(90)
    t.forward(50)
    t.backward(50)
    t.penup()
    t.setheading(90)



#drawing arms
    t.pendown()



    t.forward(50)
    t.pendown()
    t.setheading(0) 


    t.forward(40)
    t.backward(40)


    t.left(180)
    t.forward(40)
   



    
def main():
    for i in range(50):
        x = randint(-400,0)
        y = randint(-300,200)
        t.penup()
        t.goto(x,y)
        t.pendown()
        drawPizza()
        x2 = randint(0,400)
        y2 = randint(-300,300)
        t.penup()
        t.goto(x2,y2)
        t.pendown()
        drawStickMan()



main()








update()
mainloop()