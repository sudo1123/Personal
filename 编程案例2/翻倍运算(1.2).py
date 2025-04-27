import time
x=int(input("请输入您需要翻倍的数值"))
w=int(input("请输入您需要翻倍的次数"))
t=time.time()
d=0
n=0
for i in range(w):
    d=x*2
    n+=1
    x=d
    print("现在数值为",d,",这是第",n,"次翻倍.")
e=time.time()
print("程序运行了",e-t,"秒")