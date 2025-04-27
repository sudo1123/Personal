for i in range(100):
        Input=int(input("请输入你的成绩："))
        if Input<60:
            print("成绩为D")
        else:
            if Input<80:
                print("成绩为C")
            else:
                if Input<90:
                    print("成绩为B")
                else:
                    print("成绩为A")