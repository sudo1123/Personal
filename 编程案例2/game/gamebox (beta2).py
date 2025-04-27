import turtle
myPen = turtle.Pen()
a=0
myPen.speed(0)
while a<1:
    b=input()
    if b=="5":
        for c in range(10):
            d=100
            myPen.dot(10)
            myPen.reset()
            myPen.penup
            myPen.forward(10)
            myPen.pendown
            d+=1
            #if c<9:
                #myPen.reset()
    if b=="1":
        myPen.left(90)
    if b=="3":
        myPen.right(90)
    if b=="2":
        myPen.left(180)
        myPen.forward(10)
        myPen.left(180)