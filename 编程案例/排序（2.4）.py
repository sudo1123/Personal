List=[5,4,3,2,1]
def selection_sort(List):
    for i in range(len(List)):
        index=i
        for x in range(i+1,len(List)):
            if List[x]<List[i]:
                index=x
        List[i],List[index]=List[index],List[i]
    print(List)
selection_sort(List)