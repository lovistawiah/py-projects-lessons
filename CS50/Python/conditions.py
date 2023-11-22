n = int(input("Number: "))
if n > 0:
    print("n is positive")
elif n < 0:
    print("n is negative")
else:
    print("n is zero")

    # using or in the if condition to check for one of both or multiple conditions is true
    # using and in the if condition to check for both or multiple conditions are true
    # using not function to negate the statement of a condition


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(4, 5, 6))
