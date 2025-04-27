import turtle
myPen=turtle.Pen()
myPen.speed(0)
for j in range(360000):
    for i in range(4):
#外层循环多少次，左转就用360÷外层循环次数得到。
        myPen.forward(100)
        myPen.right(90)
    myPen.left(1)
    print(j)