import random

while True:
    command = input("Press 'R' to roll the dice or 'Q' to quit:").lower()

    if command == "r":
        dice_number = random.randint(1, 6)

        if dice_number == 1:
            print("+ - - - - +")
            print("|         |")
            print("|    0    |")
            print("|         |")
            print("+ - - - - +")

        elif dice_number == 2:
            print("+ - - - - +")
            print("|0        |")
            print("|         |")
            print("|        0|")
            print("+ - - - - +")

        elif dice_number == 3:
            print("+ - - - - +")
            print("| 0       |")
            print("|    0    |")
            print("|        0|")
            print("+ - - - - +")

        elif dice_number == 4:
            print("+ - - - - +")
            print("|0       0|")
            print("|         |")
            print("|0       0|")
            print("+ - - - - +")

        elif dice_number == 5:
            print("+ - - - - +")
            print("|0       0|")
            print("|    0    |")
            print("|0       0|")
            print("+ - - - - +")

        elif dice_number == 6:
            print("+ - - - - +")
            print("|0   0   0|")
            print("|         |")
            print("|0   0   0|")
            print("+ - - - - +")

    elif command == "q":
        break

    else:
        continue
