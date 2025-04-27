import turtle
myPen = turtle.Pen()
myPen.speed(0)
angle = 90
colors=["red","orange","blue","green"]
for i in range(500):
    myPen.pencolor(colors[i%4])
    myPen.forward(i)
    myPen.left(angle)
    print(i)