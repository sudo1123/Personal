S=input("请输入一个数或字符串：")
n=len(S)
result=""
for i in range(n):
    result=S[i]+result
print("这个数或字符串的倒序结果是：",result)