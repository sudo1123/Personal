import turtle
myPen = turtle.Pen()
myPen.pensize(4)
target= Input=float(input("请输入您需要找的钱数："))
money=[100,50,20,10,5,1,0.5,0.1]
number=[0,0,0,0,0,0,0,0,0]
colors=["red","blue","green","deepskyblue","puper","pink","yellow","orange","brown"]
for i in range(8):
    number[i]=target//money[i]
    target=target%money[i]
for i in range(8):
    print(money[i],"元的张数为",number[i],"张")
for i in range(8):
    myPen.pencolor(colors[i])
    myPen.forward(number[i]*30)