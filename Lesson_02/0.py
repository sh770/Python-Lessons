# random guess

import random
num = random.randint(1,10)
guessed_num=input("guess a number between 1 and 10: ")
if int(guessed_num)==num:
    print("you are corect!")
else:
    print("you are wrong..")

print("the number was:", num)