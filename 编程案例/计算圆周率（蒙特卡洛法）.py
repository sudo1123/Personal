import random
import math
d=0
e=int(input("请输入取点数量"))
print("请稍等")
for i in range(e):
    a=random.uniform(0,1)
    b=random.uniform(0,1)
    c=math.sqrt(a*a+b*b)
    if c<1:
        d=d+1
print("圆周率约为",d/e*4)
