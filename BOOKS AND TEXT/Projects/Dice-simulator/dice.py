import random
y = "y"
while y == "y":
    x = random.randint(1, 6)
    match x:
        case 1:
            print("-"*9)
            print("|       |")
            print("|   0   |")
            print("|       |")
            print("-"*9)
        case 2:
            print("-"*9)
            print("|       |")
            print("| 0   0 |")
            print("|       |")
            print("-"*9)
        case 3:
            print("-"*9)
            print("|   0   |")
            print("|       |")
            print("| 0   0 |")
            print("-"*9)
        case 4:
            print("-"*9)
            print("| 0   0 |")
            print("|       |")
            print("| 0   0 |")
            print("-"*9)
        case 5:
            print("-"*9)
            print("| 0   0|")
            print("|   0  |")
            print("| 0   0|")
            print("-"*9)
        case 6:
            print("-"*9)
            print("| 0   0 |")
            print("| 0   0 |")
            print("| 0   0 |")
            print("-"*9)
        case _:
            print("not allowed")
    y = input("enter y to roll again: ").rstrip().lstrip()
