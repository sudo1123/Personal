import time
import math
start=time.time()
t2=0
t3=0
mine=0
s=0
while True:
    end=time.time()
    t=end-start
    t2=t//1
    t3=t2//60
    if t3<1:
        if t2==1:
            print(t2,"秒")
        if t2>1:
            print(t2,"秒")
    if t3>1:
        mine=t3
        s=t2-60*t3
        print(mine,"分",s,"秒")
    if t3==1:
        mine=t3
        s=t2-60*t3
        print(mine,"分",s,"秒")
    
