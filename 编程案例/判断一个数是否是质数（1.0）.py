number=int(input("shuru："))
n=0
for i in range(2,number):
    if number % i==0:
        n=n+1
print(number,"的因数有",n+2,"个")
if n>0:
    print("这个数不是质数")
else:
    print("这个数是质数")