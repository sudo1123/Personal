import turtle
import string
myPen = turtle.Pen()
Pos=[]
o=0
k=0
c=0
for i in range(360):
    myPen.forward(1)
    myPen.left(1)
    o=o+1
    if o==180:
        Pos.append(myPen.pos())
j=Pos.split()[0]
print(j)