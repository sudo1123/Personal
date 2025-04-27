import time
z=int(input("请输入您要查找的总头数"))
u=int(input("请输入您要查找的第一选项总脚数"))
n=int(input("请输入您要查找的第二选项总脚数"))
k=int(input("请输入您要查找的总脚数"))
start=time.time()
for x in range(z):
    y=z-x
    if u*x+n*y==k:
        print("第一选项为",x,"只","第二选项为",y,"只")
end=time.time() 
print(end-start)