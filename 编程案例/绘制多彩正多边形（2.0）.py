import turtle
myPen=turtle.Pen()
myPen.pensize(4)
myPen.speed(0)
colors=["red","orange","green","pink","blue"]
length=(400)
n=(12)
for i in range(n):
    myPen.pencolor(colors[i%5])
    myPen.forward(length/n)
    myPen.right(360/n)
    print(i)