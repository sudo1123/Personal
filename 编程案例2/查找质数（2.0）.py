def prime(x):
    number=(x)
    n=0
    for i in range(2,number):
        if number % i==0:
            n=n+1
    if n>0:
        return False
    else:
        return True
z=[]
for i in range(2,101):
    if prime(i):
        z.append(i)
print(z)