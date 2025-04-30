a = int(input("請輸入a:"))#a為名稱，input a為物件
b = int(input("請輸入b:"))#b為名稱，input b為物件
print("原本a = %d，b = %d"%(a,b))
old_a = a #將a(名稱)附值於old_a(名稱)，讓old_a順著a(名稱)找到input a(物件)
a = b     #將b(名稱)附值於a(名稱)，讓a順著b(名稱)找到input b(物件)
b = old_a #將old_a(名稱)附值於b(名稱)，讓b順著old_a(名稱)->a(名稱)找到input a(物件)
print("交換以後a = %d，b = %d"%(a,b))