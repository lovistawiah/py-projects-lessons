#
# Example file for working with functions
# LinkedIn Learning Python course by Joe Marini
#


# TODO: define a basic function
def func():
    print("I am a function")

# TODO: function that takes arguments


def func1(arg1, arg2):
    print(arg1, " ", arg2)


# TODO: function that returns a value
def func2(arg1, arg2):
    return arg1 + arg2

# TODO: function with default value for an argument


def power(num, x=1):
    result = 1
    for i in range(num):
        result = result * num
        # print(result)
    return result

# TODO: function with variable number of arguments


def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result


print(func())
func()
print(func)

print(func1("Lovis", "Tawiah"))

print(func2(4, 6))

print(power(4))


print(multi_add(1, 5, 2, 56))
