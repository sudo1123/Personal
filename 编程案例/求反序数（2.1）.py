S=input("请输入一个数或字符串：")
n=len(S)
result=""
for i in range(n):
    result=result+S[n-1-i]
print("这个数或字符串的倒序结果是：",result)