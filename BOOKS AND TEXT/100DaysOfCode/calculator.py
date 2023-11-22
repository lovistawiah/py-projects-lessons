def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {'-': sub, '*': multiply, '/': divide, '+': add}
num1 = int(input("What's the first number "))
num2 = int(input("What's the second number"))
for operator in operations:
    print(operator)

operation_symbol = input("Pick an operation from the line above: ")
answer = operations[operation_symbol](num1, num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")

ask = True
while ask:
    next_question = input("Do you want to continue 'Yes' or 'No'").lower()
    if next_question == 'no':
        ask = False
    elif next_question == 'yes':
        next_number = int(input("Enter the next number: "))
        next_op = input("Enter operation symbol")
        if next_op in operations:
            next_answer = operations[next_op](answer, next_number)
            print(f"{answer} {next_op} {next_number} = {next_answer}")
