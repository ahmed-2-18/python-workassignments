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





def drawStickMan():
    
    t.pendown()
    t.setheading(0)
   
    


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

    t.penup()

    t.home()
    
    t.pendown()





def isValidNumber(number):
  

  if int(number) >= 1 and int(number) <= 10:
    return True
  else:
    print("INVALID NUMBER")
    return False
  










def main():

  print("What drawing would you like to print \n 1=stickman \n 2=pizza \n 3=rectangle \n 4=circle",)
  shapeNumber = input()
  shapeNumber =int(shapeNumber)
  if isValidNumber(shapeNumber) == True and int(shapeNumber)  <= 4 and int(shapeNumber) >= 1:
  
    
   
    print("Good choice,How much shapes would you like")
   
    userNumberOfShapes = input() ##collecting user input for choice of Shapes


    if isValidNumber(userNumberOfShapes) == True: 
      userNumberOfShapes = int(userNumberOfShapes)
      for i in range(userNumberOfShapes):
        if shapeNumber == 1:
          drawStickMan()
          t.setheading(0)
          t.penup()
          t.forward(50)
          t.pendown()
        elif shapeNumber == 2:
          drawPizza(1,"orange", "red")
          t.setheading(0)
          t.penup()
          t.forward(50)
          t.pendown()
        elif shapeNumber == 3:
          drawRectangle(20, "green")
          t.setheading(0)
          t.penup()
          t.forward(50)
          t.pendown()
        elif shapeNumber == 4:
          drawcircle(50,"red")
          t.setheading(0)
          t.penup()
          t.forward(50)
          t.pendown()

  


  else:
    print("This is not a valid option for my shapes")

main()

update()
mainloop()