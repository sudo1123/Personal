target= Input=float(input("请输入您需要找的钱数："))
money=[100,50,20,10,5,1,0.5,0.1]
number=[0,0,0,0,0,0,0,0]
for i in range(8):
    number[i]=target//money[i]
    target=target%money[i]
for i in range(8):
    print(money[i],"元的张数为",number[i],"张")