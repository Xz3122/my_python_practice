# sed = ["礫岩","石灰岩","頁岩","沙岩"]
# rock = ["礫岩","花崗岩","安山岩"]

# for num in range(len(rock)):
#     if rock[num] in sed:
#         print(rock[num]+"為沉積岩")
#     else:
#         print(rock[num]+"非沉積岩")    

sed = ["礫岩","砂岩","頁岩","粉砂岩","泥岩","石灰岩","白雲岩","燧石","煤","岩鹽","石膏"]
enter = input("請輸入岩石名稱，我會判斷是否為沉積岩:")

if enter in sed:
    print(f"{enter}為沉積岩" )
else: 
    print(f"{enter}非沉積岩" )       
    
