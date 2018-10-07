x = 3
while x > 0:
    answer = input("請輸入您的密碼:")
    if answer == "a123456":
        print("登入成功！")
        break
    else:
        x = x - 1
        if x  > 0:
            print("密碼錯誤，還有",x,"次機會")
        else:
            print("您已錯失良機！")
            break