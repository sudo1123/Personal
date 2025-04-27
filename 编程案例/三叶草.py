import turtle
myPen=turtle.Pen()
myPen.speed(1)
#for x in range(3):
for i in range(360):
        myPen.forward(1)
        myPen.left(1)
for i in range(360):
        myPen.forward(1)
        myPen.right(1)
myPen.penup()
myPen.forward(100)
myPen.goto(100,-50)
myPen.pendown()
for i in range(360):
        myPen.forward(1)
        myPen.left(1)