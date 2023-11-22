#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#

# Errors can happen in programs, and we need a clean way to handle them
# TODO: This code will cause an error because you can't divide by zero:
# print(4/0)
# TODO: Exceptions provide a way of catching errors and then handling them in
# a separate section of the code to group them together


# TODO: You can also catch specific exceptions
# try:
#     x = 10/0
# except:
#     print("didn't work")


try: 
    answer =input("What is divided by 10?")
    num = int(answer)
except ZeroDivisionError as e:
    print("Can't be divided by 0")
except ValueError as e:
    print("You didn't give a value number")
finally:
    print('this will always run')