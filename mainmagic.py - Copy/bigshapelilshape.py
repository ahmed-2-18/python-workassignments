from turtle import *
t = Turtle()
tracer(0)


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




def isValidNumber(number):
  

  if int(number) >= 1 and int(number) <= 2:
    return True
  else:
    print("INVALID NUMBER")
    return False




# def main():
#     print("What drawing would you like \n 1. A square made out of little pizzas\n 2. A square made out of mini squares.")
#     drawingOfChoice = input()
#     int(drawingOfChoice) = drawingOfChoice
#     if isValidNumber(drawingOfChoice) == True and drawingOfChoice == 1:
      
       
       





def makePizzaRowRight():
  for i in range(7): 
    drawPizza(1/7,"brown", "orange")
    t.setheading(0)
    t.penup()
    t.forward(25)
    t.pendown()



def makePizzaRowUp():
 

  # startingX = t.xcor()
  # startingY = t.ycor()

  

  for i in range(7): 
    # t.goto(startingX,startingY)

    t.setheading(0)
    t.backward(0)
    
    drawPizza(1/7,"brown", "orange")
    
  
    t.setheading(90)
    t.penup()
    t.forward(25)
    t.pendown()




makePizzaRowRight()
makePizzaRowUp()

mainloop()