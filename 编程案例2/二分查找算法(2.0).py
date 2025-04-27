number=[1,2,3,4,5,6,7,8,9,10,11,12]
target=int(input("请输入您需要查找的数"))
low=0
high=len(number)
x=0
while True:
    middle=(low+high)//2
    temp=number[middle]
    if temp==target:
        print("找到啦",temp)
        x=x+1
        break
    elif temp>target:
        high=middle-1
        x=x+1
    else:
        low=middle+1
        x=x+1
print("寻找了",x,"次")
        