with open("data.txt","r") as f:
    content=f.read()
print(content)
List = content.split(" ")
print(len(List)-1)