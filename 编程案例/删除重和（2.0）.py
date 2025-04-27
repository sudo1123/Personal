student=[1,2,1,3,5,4,4,6]
student_2=[]
for x in student:
    if x not in student_2:
        student_2.append(x)
print(student_2)