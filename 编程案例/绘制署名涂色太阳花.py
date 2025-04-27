import turtle
myPen=turtle.Pen()
myPen.speed(0)
myPen.pensize(3)
myPen.pencolor("red")
myPen.fillcolor("red")
title="太阳花"
name="X战警"
box=[title,name]
myPen.begin_fill()
for l in range(90):
    for i in range(4):
        myPen.forward(100)
        myPen.left(90)
    myPen.left(4)
myPen.end_fill()
myPen.penup()
myPen.goto(150,-50)
myPen.pendown
myPen.write(box[0],font=("Arial",30))
myPen.penup()
myPen.goto(150,-150)
myPen.pendown
myPen.write(box[1],font=("Arial",30))