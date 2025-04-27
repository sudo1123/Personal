import turtle
myPen=turtle.Pen()
myPen.speed(0)
def polygon(x,y):
    for i in range(x):
        myPen.forward(y)
        myPen.left(360/x)
for i in range(50):
    polygon(i+3,30)