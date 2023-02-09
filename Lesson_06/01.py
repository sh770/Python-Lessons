import random

x = random.randint(1,10)
print(x)
y = input("enter num: ")
def run():

    if x == y:
        print("you win",x)
        input("Press Enter to exit")
    else:
        print("yor lost tray egen")
        y = input("enter num: ")

        # run()
        
    # y = input("enter num: ")
# print("num is: ",x)    
# input("Press Enter to exit")

run()