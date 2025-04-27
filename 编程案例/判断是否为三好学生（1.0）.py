for i in range(100):
    Input_1=int(input("请输入你的语文成绩："))
    Input_2=int(input("请输入你的数学成绩："))
    Input_3=int(input("请输入你的英语成绩："))
    if Input_1>90:
        if Input_2>90:
            if Input_3>90:
                print("你是三好学生")
            else:
                print("你不是三好学生")
        else:
            print("你不是三好学生")
    else:
        print("你不是三好学生")