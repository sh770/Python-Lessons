# # Plan to roll 2 dice and print their values to the screen, where O represents the result

# import random

# # Roll the dice
# dice1 = random.randint(1, 6)
# dice2 = random.randint(1, 6)

# # Print the results
# print("O" * dice1)
# print("O" * dice2)
# Plan to roll 2 dice and print their values to the screen in the form of a dice

import random

def print_dice(value):
    if value == 1:
        print(" _______ ")
        print("|       |")
        print("|   O   |")
        print("|       |")
        print(" _______ ")
    elif value == 2:
        print(" _______ ")
        print("| O     |")
        print("|       |")
        print("|     O |")
        print(" _______ ")
    elif value == 3:
        print(" _______ ")
        print("| O     |")
        print("|   O   |")
        print("|     O |")
        print(" _______ ")
    elif value == 4:
        print(" _______ ")
        print("| O   O |")
        print("|       |")
        print("| O   O |")
        print(" _______ ")
    elif value == 5:
        print(" _______ ")
        print("| O   O |")
        print("|   O   |")
        print("| O   O |")
        print(" _______ ")
    elif value == 6:
        print(" _______ ")
        print("| O   O |")
        print("| O   O |")
        print("| O   O |")
        print(" _______ ")

# Roll the dice
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)

# Print the results
print_dice(dice1)
print_dice(dice2)
