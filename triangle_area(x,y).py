import math

x1 = float(input("Enter x1:"))
y1 = float(input("Enter y1:"))
x2 = float(input("Enter x2:"))
y2 = float(input("Enter y2:"))
x3 = float(input("Enter x3:"))
y3 = float(input("Enter y3:"))

def Heron(a,b,c):
    s = (a + b + c)/2
    return math.sqrt(s*(s-a)*(s-b)*(s-c))
    

def side(x1,y1,x2,y2,x3,y3):
    a = math.sqrt(pow((x2-x1),2)+pow((y2-y1),2))
    b = math.sqrt(pow((x3-x2),2)+pow((y3-y2),2))
    c = math.sqrt(pow((x1-x3),2)+pow((y1-y3),2))
    return(a,b,c)

def is_triangle(a,b,c):
    return a + b > c and a + c > b and b + c > a
    
a,b,c = side(x1,y1,x2,y2,x3,y3)
print(f"side a = {a:.2f},side b = {b:.2f},side c = {c:.2f}")

area =  Heron(a,b,c)
if is_triangle(a,b,c):
    print(f"triangle arar = {area:.2f}")
else:
    print("That is not triangle!")
