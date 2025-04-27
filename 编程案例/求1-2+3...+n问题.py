Sum=0
n=int(input("请输入n的值"))
for i in range(1,n+1):
    if i%2==0:
        Sum=Sum+i*-1
    else:
        Sum=Sum+i
print(Sum)