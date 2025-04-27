import turtle
myPen=turtle.Pen()
myPen.pensize(4)
myPen.speed(0)
colors=["red","orange","green","pink","blue"]
length=(600)
n=(5)
for i in range(n):
    myPen.pencolor(colors[i])
    myPen.forward(length/n)
    myPen.right(360/n)