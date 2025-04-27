a = int(input("请输入您选择的模式（1代表加法运算,2代表减法运算,3代表除法运算,4代表乘法运算,5代表乘方运算）"))
if a == 1:
    b = int(input("请输入一个加数"))
    c = int(input("请输入另一个加数"))
    d = c+b
    print("结果是", d)
if a == 2:
    e = int(input("请输入被减数"))
    f = int(input("请输入减数"))
    g = e-f
    print("结果是", g)
if a == 3:
    h = int(input("请输入被除数"))
    j = int(input("请输入除数"))
    if j == 0:
        print("您输入的除数是0，0不能作为除数")
    else:
        k = h/j
        print("结果是", k)
if a == 4:
    l = int(input("请输入一个乘数"))
    m = int(input("请输入另一个乘数"))
    n = l*m
    print("结果是", n)
if a == 5:
    o = int(input("请输入底数"))
    p = int(input("请输入指数"))
    for q in range(p):
        r = o*o
    print("结果是", r)
