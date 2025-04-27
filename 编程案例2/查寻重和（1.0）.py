student=["1","2","1","3","5","4","4","6"]
for i in range(0,len(student)):
    for x in range(i+1,len(student)):
        if student[i]==student[x]:
            print("重和的是",student[i],"在列表第",i+1)