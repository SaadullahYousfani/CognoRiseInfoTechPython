#Dice Rolling Simulator: 

import random 

def dice_roll(num_of_sides, num_of_rolls):
    print(f"Rolling a {num_of_sides} - sided dice {num_of_rolls} times: ")
    for roll in range(1, num_of_rolls + 1):
        result = random.randint(1, num_of_sides)
        print(f"Roll {roll}: {result}")

def play_dice():
    print("Welcome to Dice Rolling Simulator :)")
    while True:
        try:
            num_of_sides  = int(input("Enter the number of sides on the dice: "))
            num_of_rolls = int(input("Enter the number of rolls: "))
            if num_of_sides <= 0 or num_of_rolls <= 0:
                print("Please enter positive integers for the number of sides and rolls. ")
            else:
                dice_roll(num_of_sides, num_of_rolls)
                break
        except ValueError:
            print("Please enter valid integers for the number of sides and rolls")


if __name__ == "__main__":
    play_dice()
