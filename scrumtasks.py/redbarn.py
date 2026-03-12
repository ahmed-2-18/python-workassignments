from random import *
from turtle import *


tracer(100)



t=Turtle()

def drawBarn():
    
    
    t.color("#5A1B1B")
    t.begin_fill()



    for i in range(2):
        t.forward(200)

        t.left(90)

        t.forward(125)
        t.left(90)


    t.end_fill()
    t.penup()

    ##Top Left OF RECTANGLE READY TO DRAW ROOF
    t.left(90)
    t.forward(125)
    
    
  
    
    ##preparing to draw roof 


    ## do 180/4 for hexagon roof

    t.pendown()
    t.color("#ece6e6")
    t.begin_fill()
   
    t.right(90)
    t.forward(200)  
    t.left(127)
       
    

    for i in range(4): 
          t.forward(65)
          t.left(180/5)
         
    t.end_fill()  
    t.setheading(270) 
    


    # window left
    t.penup()
    t.color("#000000")
    
    t.forward(45)
    t.begin_fill()
    t.left(90)
    t.forward(10)
    t.pendown()
    

   
    
    for i in range(4):
        t.forward(45)
        t.left(90)
    t.end_fill()

##right window
    t.penup()

    t.forward(130)

    t.pendown()
    t.begin_fill()
    for i in range(4):
        t.forward(45)
        t.left(90)
    t.end_fill()



    ## going to draw x
    t.penup()
    t.left(180)
    t.forward(45)

    
    t.pendown()
    t.color("white")

    t.right(45)
    t.forward(45)
    t.backward(90)
    t.forward(45)
    t.right(90)
    t.forward(45)
    t.backward(90)
    
    


    
      
    
    


    









   
drawBarn()        





update()
mainloop()