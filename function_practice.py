import math

a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))

def Heron(a,b,c):#函式必須要放在(呼叫)前
    s = (a + b + c)/2
    return math.sqrt(s*(s-a)*(s-b)*(s-c))

if a + b > c and a + c > b and b + c > a:
   print("Triangle area is", Heron(a, b, c))
else:
   print("Invalid triangle sides.")  
   

