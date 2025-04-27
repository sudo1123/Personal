import random
a=input("please input your code:")
c=[]
f=[]
h=[]
i=[]
b=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z" ,"1","2","3","4","5","6","7","8","9","0"]
c= a.split(" ")
for e in range(len(c)):
    for g in range(len(b)):
        if c[e]==b[g]:
            h.append(g)
l=random.randint(1,len(h)-1)
for j in range(len(h)):
    if 0<g-l<len(h)-1:
        i.append(h[j-l])
    else:
        k=-(j-1)
        i.append(h[k])
print("this is your code:",i)
print("this is your key:",l)
