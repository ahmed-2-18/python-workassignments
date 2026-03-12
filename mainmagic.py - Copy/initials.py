from turtle import *


initial = Turtle()

def drawA():
    #record starts
    
    start_x =initial.xcor()
    start_y = initial.ycor()
    
    initial.left(50)
    initial.forward(50)
    initial.right(100)
    initial.forward(50)
    initial.backward(25)
    initial.left(230)
    initial.forward(30)
    initial.penup()
    initial.goto(start_x + 60, start_y)
    initial.setheading(0)
    initial.pendown()

def drawT():
    
    start_x = initial.xcor()
    start_y = initial.ycor()


   

    initial.pendown()
    initial.left(90)
    initial.forward(50)
    initial.left(90)
    initial.forward(25)
    initial.right(180)
    initial.forward(50)
    initial.penup()
    initial.goto(start_x + 60, start_y)
    initial.pendown() 


#drawA()
drawA()

drawT()




mainloop()