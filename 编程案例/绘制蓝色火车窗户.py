import turtle
myPen=turtle.Pen()
myPen.pencolor("blue")
myPen.pensize(4)
for z in range(6):
    for i in range(4):
        myPen.forward(50)
        myPen.right(90)
    myPen.penup()
    myPen.goto(70*(z+1),0)
    myPen.pendown()
    print(z)