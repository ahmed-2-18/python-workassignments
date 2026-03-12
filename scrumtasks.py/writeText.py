from turtle import *



t=Turtle()


def writeText(color):
    t.color(color)
    t.penup()
    t.goto(325,-375)
    t.pendown()
    t.write("Ahmed, Kahari, Lucy, Zoe", align='left')





writeText("Red")

update()
mainloop()