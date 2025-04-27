#with open("data_2.txt", "r") as f:
    #content = f.read()
content=1.,2.,3.,4.,5.
print(content)
newcontent = content.replace(".","")
newcontent_2=newcontent.split(" ")
print(newcontent_2)
print(len(newcontent_2))
Join=" ".join(newcontent_2)
print(Join)
with open("data.txt", "w") as f:
     f.write(Join)
