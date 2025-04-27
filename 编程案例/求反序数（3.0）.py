def reverse(x):
    number=x
    S=str(number)
    n=len(S)
    result=""
    for i in range(n):
        result=S[i]+result
    print("这个数或字符串的倒序结果是：",int(result))
reverse(123456)