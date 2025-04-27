import turtle
myPen = turtle.Pen()
a=0
myPen.speed(0)
while a<1:
    b=input()
    if b=="5":
        myPen.forward(10)
    if b=="1":
        myPen.left(90)
    if b=="3":
        myPen.right(90)
    if b=="2":
        myPen.left(180)
        myPen.forward(10)
        myPen.left(180)