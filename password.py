password = 123
count = 5

while count > 0:
    you = int(input("Please enter password : "))
    if you == password:
        print("Login Successful")
        break
    else:
        count -= 1
        if count > 0:
            print("Login again，you have {} chance".format(count))
        else:
            print("You have no chance")     
    
  