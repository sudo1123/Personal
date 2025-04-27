import time
z=time.time()
number=[1,2,3,4,5,6,7,8,9,10,11,12,]
print("你输入的数串最大值为",len(number))
y=time.time()
target=int(input("请输入你需要找的数"))
m=time.time()
low=0
high=len(number)
x=0
while True:
    middle=(low+high)//2
    temp=number[middle]
    if temp==target:
        print("找到啦",temp)
        x+=1
        break
    elif temp>target:
        high=middle-1
        x+=1
    else:
        low=middle+1
        x+=1
print("寻找了",x,"次")
v=time.time()
u=v-m+y-z
print("程序运行了",u,"秒")