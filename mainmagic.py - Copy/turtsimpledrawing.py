from turtle import *


t = Turtle()

def drawPizza():
    t.speed(5)
    t.penup()
    #t.goto(0, -100)
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
    t.penup()
    #t.goto(0,0)
    t.left(90)
    t.forward(85)
    for i in range(8):
        t.pendown()
        t.forward(85)
        t.penup()
        t.left(180)
        t.forward(85)
        t.left(45)


drawPizza()
t.goto(100,0)
drawPizza()



mainloop()