#求2的倍數但不是3的倍數
n = int(input())
print("1~%d中2的倍數但不是3的倍數有:"%n)

for i in range(2,n,2):
    if (i%3) != 0:
        print(i)


    