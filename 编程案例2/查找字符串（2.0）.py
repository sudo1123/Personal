a=input("请输入您的文本或数值：")
b=input("请输入您需要查找的文本或数值：")
number=0
for i in range(len(a)):
    if a[i:i+3]==b:
        number=number+1
        print("找到啦,在",a,"中的索引位置为",i,"至",i+3)
print(b,"在",a,"中出现了",number,"次")