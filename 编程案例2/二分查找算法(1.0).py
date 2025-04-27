number=[1,2,3,4,5,6,7,8,9,10]
target=10
low=0
high=len(number)
x=0
while True:
    middle=(low+high)//2
    temp=number[middle]
    if temp==target:
        print("找到啦",temp)
        break
    elif temp>target:
        high=middle-1
    else:
        low=middle+1
        