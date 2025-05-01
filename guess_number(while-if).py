import random

answer = random.randint(1, 100)
n = int(input("Please enter number 1~100: "))

if n > answer:
    print("Too large!")
elif n < answer:
    print("Too small!")
else:
    print("That's right!")

# while 迴圈代表至少執行 0 次，但猜數字至少要執行 1 次
while n != answer:
    n = int(input("Please enter number 1~100: "))
    if n > answer:
        print("Too large!")
    elif n < answer:
        print("Too small!")
    else:
        print("That's right!")
        break
    
# import random

# answer = random.randint(1, 100)

# while True:
#     n = int(input("Please enter number 1~100 : "))
#     if n > answer:
#         print("Too large!")
#     elif n < answer:
#         print("Too small!")
#     else:
#         print("That's right!")
#         break    
    
    
    
    