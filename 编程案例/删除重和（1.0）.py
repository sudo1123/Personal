student=[1,2,1,3,5,4,4,6]
List_name=[]
for i in range(0,len(student)):
    for x in range(i+1,len(student)):
        if student[i]==student[x]:
            List_name.append(x)
List_name2=sorted(List_name,reverse=True)
for z in List_name2:
    student.pop(z)
print(student)
    