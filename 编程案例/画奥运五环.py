import turtle
myPen=turtle.Pen()
myPen.pensize(5)
Pos=[(0,0),(100,0),(50,-55),(-50,-55),(-100,0)]
Colors=["black","red","green","yellow","blue"]
for i in range(5):
    myPen.penup()
    myPen.goto(Pos[i])
    myPen.pendown()
    myPen.pencolor(Colors[i])
    myPen.circle(50)