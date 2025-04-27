import turtle


myPen = turtle.Pen()
myPen.speed(0)
angle = 90
for i in range(400):
    myPen.forward((i * 1.1))
    myPen.left(angle)
    print(i)
