x = 1
y = input("enter number: ")
y = int(y)
while x <= y:
    if x % 7 == 0:
        print("BOOM!")
    else:
        print(x)    
    x += 1     
input("Press Enter to exit")