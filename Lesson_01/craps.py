import random

sum = random.randint(1,6)+ random.randint(1,6) 
print("You got " + str(sum))

if sum == 7 or sum == 11: 
    print("You win!")

elif sum == 2 or sum == 3 or sum == 12: 
    print("You lose")

else: 
    sum2 = random.randint(1,6) + random.randint(1,6) 
    if sum2 == sum:
        print("You win in second trial")
    elif sum2 == 7:
        print("You lose in second trial")
    else:
        print("You don't win or lose")