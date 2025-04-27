a=0
b=1
e=int(input("请输入您需要的范围（10的倍数）"))
for c in range(1,10):
    d=2*c-1
    if b==1:
        a+=1/d
    else:
        a-=1/d
    print(4*a)
    b=b*-1
