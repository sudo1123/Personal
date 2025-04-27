from pyecharts import Bar
import json
import webbrowser
import os
with open("birthday.json","r") as f:
    x=json.load(f)
month=[0]*12
for i in x:
    month[int(i)-1] += 1
a_asis=[1,2,3,4,5,6,7,8,9,10,11,12]
b_asis=month
bar=Bar("生日统计")
bar.add("",a_asis,b_asis)
bar.render()
webbrowser.open("file://"+os.path.realpath("render.html"))