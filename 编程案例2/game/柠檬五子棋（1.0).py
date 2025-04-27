import turtle
myPen=turtle.Pen()
myPen.speed()
a=int(input("请输入棋盘长宽"))
b=int(input("请输入棋盘格长宽（必须是棋盘长宽因数）"))
c=b
myPen.left(90)
for i in range(int(a/c)):
    myPen.forward(a)
    myPen.penup()
    myPen.goto(b,0)
    myPen.pendown()
    b=b+c
myPen.goto(a,0)
myPen.forward(a)
myPen.penup()
myPen.goto(0,0)
myPen.pendown()
myPen.right(90)
b=0
for r1 in range(int(a/c)):
    myPen.forward(a)
    myPen.penup()
    myPen.goto(0,b)
    myPen.pendown()
    b=b+c
myPen.goto(0, a-c)
myPen.forward(a)
myPen.penup()
myPen.goto(0, a)
myPen.pendown()
myPen.forward(a)
def qu(o):
    o=o+a/2
w2=[]
qq1=0
qq=int(a/c)
for r3 in range(qq):
    w2.append(str(qq1))
    qq1=qq1+1
b=0
for r2 in range(int(a/c)):
    myPen.penup()
    myPen.goto(0-c-4,b-c)
    myPen.pendown()
    myPen.write(w2[r2])
    b=b+c
myPen.penup()
myPen.goto(0-c-4,a-c)
myPen.pendown()
myPen.write("10")
b=0
w2.pop(0)
for r2 in range(int(a/c-1)):
    myPen.penup()
    myPen.goto(b+c,0-c-4)
    myPen.pendown()
    myPen.write(w2[r2])
    b=b+c
myPen.penup()
myPen.goto(a,0-c-4)
myPen.pendown()
myPen.write("10")
jishu=0
while True:
    Inp=int(input("请输入横坐标"))
    Inp2=int(input("请输入纵坐标"))
    p1=Inp*c
    p2=Inp2*c
    jishu=jishu+1
    myPen.penup()
    myPen.goto(p1,p2)
    myPen.pendown()
    if jishu%2==0:
        myPen.color("blue")
        myPen.dot(c/2)
    else:
        myPen.color("black")
        myPen.dot(c/2)
turtle.done()