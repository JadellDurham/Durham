#Learn how to use turtle graphics
#9/24/19
#CTI-110 P2HW2 - Turtle Graphic
#Jadell Durham

import turtle
wn = turtle.Screen()
wn.bgcolor('lightblue')

tim = turtle.Turtle()
tim.color("red", "blue")
tim.shape('turtle')

tim.begin_fill()
tim.left(45)
tim.forward(100)
tim.right(90)
tim.forward(100)
tim.end_fill()
tim.begin_fill()
tim.forward(100)
tim.left(90)
tim.forward(100)
tim.left(90)
tim.forward(100)
tim.left(90)
tim.forward(200)
tim.right(90)
tim.forward(100)
tim.end_fill()

wn.mainloop()

