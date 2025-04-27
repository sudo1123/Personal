def reverst(X):
    number=X
    mums=[]
    n=len(str(number))
    result=0
    for i in range(n):
        mums.append(number%10)
        number=number//10
    for i in range(n):
        result=result*10+mums[i]
    print(result)
reverst(12345)