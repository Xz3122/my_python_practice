acount = []
password = []   
count = 5
passcount = 5

myacount = input("請設定帳號:")
mypassword = input("請設定密碼:")
acount.append(myacount)
password.append(mypassword)

while count > 0 :
    my = input("請輸入帳號:")
    if my == myacount :
        while count > 0 :
            me = input("請輸入密碼:")        
            if me == mypassword :
                print("恭喜你完成登入")
                exit()
            else:
                passcount-=1
                print(f"密碼錯誤，你還有{passcount}次機會!")
                if passcount == 0:
                    print("你的帳號密碼已經鎖死") 
                    break  
    
    else:
        count-=1
        print(f"帳號錯誤，你還有{count}次機會!")
        if count == 0:
            print("你的帳號密碼已經鎖死")
            break

        
