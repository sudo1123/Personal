import time
import math
start=time.time()
def prime(x):
    number=(x)
    for i in range(2,int(math.sqrt(number))+1):
        if number % i==0:
            return False
    return True
z=[]
for i in range(2,10001):
    if prime(i):
        z.append(i)
print("共找到",len(z),"个质数")
end=time.time()
print("这个程序的运行时间为",end-start,"秒")