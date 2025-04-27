def prime(x):
    number=(x)
    for i in range(2,number):
        if number % i==0:
            return False
    return True
z=[]
for i in range(2,101):
    if prime(i):
        z.append(i)
print(z)