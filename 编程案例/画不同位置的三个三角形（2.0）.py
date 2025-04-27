import turtle
myPen=turtle.Pen()
myPen.speed(0)
def square(x):
    for i in range(3):
        myPen.forward(x)
        myPen.left(120)
def moveto(x,y):
    myPen.penup()
    myPen.goto(x,y)
    myPen.pendown()
A=65
B=77
C=33
D=56
E=12
F=23
square(A)
moveto(60,7)
square(B)
moveto(85,1)
square(C)
moveto(19,99)
square(D)
moveto(-1,80)
square(E)
moveto(60,7)
square(F)
moveto(10,7)