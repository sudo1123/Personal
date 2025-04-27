import time
import math
start=time.time()
v=int(input("请输入您要查找的质数范围：（注意要加一）:"))
def prime(x):
    number=(x)
    if number==1:
        print(number,"不是质数")
        return False
    for i in range(2,int(math.sqrt(number))+1):
        if number % i==0:
            return False
    return True
z=[]
for i in range(2,v):
    if prime(i):
        z.append(i)
print("共找到",len(z),"个质数")
print(z)
end=time.time()
print("这个程序的运行时间为",end-start,"秒")