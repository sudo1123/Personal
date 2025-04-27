for i in range(100):
    Input_1=int(input("请输入你的语文成绩："))
    Input_2=int(input("请输入你的数学成绩："))
    Input_3=int(input("请输入你的英语成绩："))
    Input_4=int(input("请输入你的体育成绩："))
    if Input_1>90 and Input_2>90 and Input_3>90 and Input_4>90:
        print("恭喜你成为三好学生")
    elif Input_1<60 or Input_2<60 or Input_3<60 or Input_4<60:
        print("别灰心，下次努力")
    else:
        print("再接再厉，争取成为三好学生")
    