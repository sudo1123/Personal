List=[5,4,3,2,1]
for j in range(len(List)):
    index=j
    for i in range(j+1,len(List)):
        if List[i]<List[index]:
            index=i
    temp=List.pop(index)
    List.insert(j,temp)
print(List)

