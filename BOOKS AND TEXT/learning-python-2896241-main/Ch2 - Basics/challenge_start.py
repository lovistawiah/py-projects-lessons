# ask user for input


def isNumber(text):
    if text == text[::-1]:
        print(text, "is a palindrome")
    else:
        print(text, " is not a palindrome")


def isString(text):
    if text == text[::-1]:
        print(text, "is a palindrome")
    else:
        print(text, " is not a palindrome")


string = input("enter a palindrome or type exit")

if string == "exit":
    print("program exited")
else:
    if string.isnumeric():
        isNumber(string)
    else:
        isString(string)
