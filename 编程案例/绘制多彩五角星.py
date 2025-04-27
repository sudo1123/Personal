import turtle
myPen = turtle.Pen()
myPen.speed(0)
angle = 144
n=6
length=25
colors=["red","green","blue"]
for i in range(5):
    for j in range(n):
        myPen.pencolor(colors[j%3])
        myPen.forward(length)
    myPen.right(angle)