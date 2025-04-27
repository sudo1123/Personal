from pyecharts import Bar
import json
with open("birthday.json","r") as f:
    x=json.load(f)
month=[0]*12
for i in x:
    month[int(i)-1] += 1
print(month)
    