a = int(input("輸入梯形上底 a:"))
b = int(input("輸入梯形下底 b:"))
c = int(input("輸入梯形高度 c:"))

def trapezoid(a,b,c):
    area = ((a + b) * c)/2 
    return area
print("trapezoid area:",trapezoid(a,b,c))