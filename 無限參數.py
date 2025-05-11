msgs = input("請輸入你想講的內容:")

def say(*msgs): # * 可以傳入任意多個參數，這些參數會被收集成一個tuple，變數名稱為 msgs
    for i in msgs:
        print(i)
        
say(*msgs)       