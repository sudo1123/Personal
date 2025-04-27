Dict={"a":89, "b":30, "c":45, "d":100}
keys=[]
z=[]
x=0
name=""
Max=0
for l in Dict:
    keys.append(l)
for i in range(4):
    z.append(Dict[keys[i]])
    if z[i]>Max:
        Max=z[i]
        x=i
        name=keys[x]
print(name,"的成绩最高，为",Max,"分")