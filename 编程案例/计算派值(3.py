import turtle
import string
myPen = turtle.Pen()
Pos=[]
o=0
k=0
c=0
j=1
r=360*j
py=r/2
myPen.speed(0)
for i in range(int(py)):
    print(i+1)
    myPen.forward(1)
    myPen.left(1/j)
    o=o+1
    if o==r/2:
        Pos.append(myPen.pos())
print(Pos)
m=float(input(6))
t=r/m
print(t)