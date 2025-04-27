import turtle
import string
myPen = turtle.Pen()
Pos=[]
o=0
k=0
c=0
j=1
r=360*j
myPen.speed(10)
for i in range(r):
    myPen.forward(1)
    myPen.left(1/j)
    o=o+1
    if o==180:
        Pos.append(myPen.pos())
print(Pos)
m=float(input(6))
t=r/m
print(t)