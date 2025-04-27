a = (int(input("请输入范围")))
b = 1
c=0
d=[]
for i in range(2):
    d.append(b)
for e in range(a):
    f=d[e]+d[e+1]
    d.append(f)
print(d)
