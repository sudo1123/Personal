Dict={"a":100, "b":100, "c":1, "d":100}
keys=[]
z=[]
x=0
y=[]
name=""
Max=0
Sum=0
average=0
for l in Dict:
    keys.append(l)
for i in range(len(keys)):
    z.append(Dict[keys[i]])
    if z[i]>Max:
        Max=z[i]
        x=i
        name=keys[x]
    y.append(i)
print(name,"的成绩最高，为",Max,"分")
Min=Max
for i in range(len(keys)):
    z.append(Dict[keys[i]])
    if z[i]<Min:
        Min=z[i]
        x=i
        name=keys[x]
print(name,"的成绩最低，为",Min,"分")
for l in Dict:
    Sum=Sum+Dict[l]
average=Sum/len(keys)
print("这个班的总分为",Sum,"分")
print("这个班的平均分为",average,"分")