# Plan to roll 2 dice and print their values to the screen in the form of a dice. Continuously rolls the dice until 'Q' is pressed, and summarizes the value of the rolls and the percentage of each outcome.

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

outcomes = [0, 0, 0, 0, 0, 0]
total_rolls = 0

while True:
    # Roll the dice
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total_rolls += 1
    outcome = dice1 + dice2
    # outcomes[outcome - 2] += 1
    outcomes[min(outcome - 2, len(outcomes) - 1)] += 1

    # Print the results
    print_dice(dice1)
    print_dice(dice2)
    print("\n")

    # Ask if the user wants to roll again
    roll_again = input("Press Enter to roll again, or Q to quit: ")
    if roll_again == "q":
        break

    # Summarize the results
for i in range(2, 13):
    # percentage = outcomes[i - 2] / total_rolls * 100
    percentage = outcomes[min(max(i - 2, 0), len(outcomes) - 1)] / total_rolls * 100
    # print(f"{i}: {outcomes[i - 2]} ({percentage:.2f}%)")
    print(f"{i}: {outcomes[min(max(i - 2, 0), len(outcomes) - 1)]} ({percentage:.2f}%)")