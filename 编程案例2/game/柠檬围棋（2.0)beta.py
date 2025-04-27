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
we1=str(a//c)
myPen.write(we1)
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
we=str(a//c)
myPen.write(we)
jishu=0
def draw():
    a = a
    b = c
    myPen.left(90)
    for i in range(int(a/c)):
        myPen.forward(a)
        myPen.penup()
        myPen.goto(b, 0)
        myPen.pendown()
        b = b+c
    myPen.goto(a, 0)
    myPen.forward(a)
    myPen.penup()
    myPen.goto(0, 0)
    myPen.pendown()
    myPen.right(90)
    b = 0
    for r1 in range(int(a/c)):
        myPen.forward(a)
        myPen.penup()
        myPen.goto(0, b)
        myPen.pendown()
        b = b+c
    myPen.goto(0, a-c)
    myPen.forward(a)
    myPen.penup()
    myPen.goto(0, a)
    myPen.pendown()
    myPen.forward(a)

    def qu(o):
        o = o+a/2
    w2 = []
    qq1 = 0
    qq = int(a/c)
    for r3 in range(qq):
        w2.append(str(qq1))
        qq1 = qq1+1
    b = 0
    for r2 in range(int(a/c)):
        myPen.penup()
        myPen.goto(0-c-4, b-c)
        myPen.pendown()
        myPen.write(w2[r2])
        b = b+c
    myPen.penup()
    myPen.goto(0-c-4, a-c)
    myPen.pendown()
    we1 = str(a//c)
    myPen.write(we1)
    b = 0
    w2.pop(0)
    for r2 in range(int(a/c-1)):
        myPen.penup()
        myPen.goto(b+c, 0-c-4)
        myPen.pendown()
        myPen.write(w2[r2])
        b = b+c
    myPen.penup()
    myPen.goto(a, 0-c-4)
    myPen.pendown()
    we = str(a//c)
    myPen.write(we)
while True:
    Inp=int(input("请输入横坐标"))
    Inp2=int(input("请输入纵坐标"))
    p1=Inp*c
    p2=Inp2*c
    jishu=jishu+1
    myPen.penup()
    myPen.goto(p1,p2)
    myPen.pendown()
    zb=[]
    zb1=[]
    if jishu%2==0:
        myPen.color("blue")
        myPen.dot(c/2)
        zb.append(myPen.pos())
    else:
        myPen.color("black")
        myPen.dot(c/2)
        zb1.append(myPen.pos())
    ro = 0
    Pos=0
    for r4 in range(len(zb1)):
        if len(zb)==0:
            op=0
        else:
            Pos=zb[r4]
            Pos1 = str(Pos)
            Pos2 = Pos1.split("(")
            Pos3 = Pos2[1].split(")")
            Pos4 = Pos3[0].split(",")
            Poss=zb1[r4]
            Poss1=str(Pos)
            Poss2 = Poss1.split("(")
            Poss3 = Poss2[1].split(")")
            Poss4 = Poss3[0].split(",")
            if Pos4[0]==Poss4[0]-c:
                if Pos4[1]==Poss4[1]:
                    ro=ro+1
            if Pos4[0]==Poss4[0]+c:
                if Pos4[1] == Poss4[1]:
                    ro = ro+1
            if Pos4[1]==Poss[1]+c:
                if Pos4[0]==Poss4[0]:
                    ro=ro+1
            if Pos4[1] == Poss[1]-c:
                if Pos4[0] == Poss4[0]:
                    ro = ro+1#判断蓝子是否被黑子围
        if ro==4:
            myPen.reset()#清屏
            draw()
turtle.done()
