from turtle import *
from random import *
tracer(0)


t = Turtle()
## pizza
def drawPizza(size,crustColor,innerColor):
   

    t.speed(10)
    t.penup()
    
    t.right(90)
    t.forward(100*size)
    t.setheading(0)
    t.pendown()
    t.color(crustColor)
    t.begin_fill()
    t.circle(100*size)
    t.end_fill()
   
    t.penup()
    #t.goto(0, -85)
    t.left(90)
    t.forward(15*size)
    t.setheading(0)
    t.pendown()
    t.color(innerColor)
    
    #color of inner circle
    t.begin_fill()

    t.circle(85*size)
    t.end_fill()

    #slices
    t.color("black")
    
    t.left(90)
    t.forward(85*size)
    for i in range(8):
        t.pendown()
        t.forward(85*size)
        t.penup()
        t.left(180)
        t.forward(85*size)
        t.left(45)


## circle
def drawcircle(size,colorFill):
    t.color(colorFill)
    t.begin_fill()
    t.circle(size)



##rectangle 
def drawRectangle(size,color):
    t.begin_fill()
    t.color(color)

    t.forward(size)
    t.left(90)
    t.forward(size+50)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size+50)











def main():
    
    t.penup()
    t.goto(-150,0)
    t.pendown()
    drawRectangle(15,"red")
    t.penup()
    t.goto(100,0)
    t.pendown()
    drawcircle(50,"blue") 
    t.penup()
    t.goto(-300,0)
    t.pendown()
    drawPizza(1,"green","purple")
    t.penup()
    goto(-100,0)
    t.penup()
    t.goto(25,0)
    t.pendown()
    drawRectangle(25,"orange")
    t.penup()
    t.goto(86,0)
    t.pendown()
    drawcircle(9,"Green") 
    t.penup()
    t.goto(-240,-20)
    t.pendown()
    drawPizza(.5,"red","purple")
    
    

main()
mainloop()