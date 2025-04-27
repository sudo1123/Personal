import turtle
myPen=turtle.Pen()
a=float(input("请输入二次项系数"))
b=float(input("请输入一次项系数"))
c=float(input("请输入常数项"))
e=0
f=int(input("请输入取点数量"))
j=float(input("请输入取点间距"))
d=0-f/2
for i in range(f):
    e=d*d*a+d*b+c
    if i==0:
        myPen.penup()
        myPen.goto(d,e)
        myPen.pendown()
    else:
        myPen.goto(d,e)
        d=d+j
myPen.penup()
myPen.goto(0,0)
myPen.pendown()
myPen.write("0")
myPen.goto(e,0)
myPen.write("x")
myPen.goto(0-e,0)
myPen.penup()
myPen.goto(0,0)
myPen.pendown()
myPen.goto(0,e)
myPen.write("y")
myPen.goto(0,0-e)
turtle.done
