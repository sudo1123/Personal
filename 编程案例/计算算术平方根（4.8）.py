x = float(input("请输入需要求算术平方根的数："))
b = 0
z = 0
v = z+1
k = 1
w = 0
d = int(input("需要的精确度（输入的整数数值越高计算无限小数型的算术平方根数值越精确，如果不能确定是否为无限不循环小数，推荐输入10000）："))
u = []
e = 0
for y in range(d):
    for i in range(10):
        b = v*v
        if b < x:
            v = v+k
            d = d+1000
        if b > x:
            print("这个数的算术平方根是无限小数，现在精确到：", v)
            w = v
            v = v/10
            k = k/10
        if b == x:
            u.append(v)
            e = len(u)
            for q in range(e-1):
                 u.pop()
if u == []:
    print()
else:
    pre = u[0]
    print("这个数的算术平方根是：", pre)
