"""
Strings are sequence of characters
It is object oriented 
Strings are case-sensitive
all strings are unicode
they're index of characters starting from 0
Get the size of a string using len() function
slice syntatic sugar stringVariable[num1 : num2] meaning start at num1 up to num2 but not including num2
replace method: accepts two string arguments, the old characters of string or character and the string to replace the old one
rstrip() method: strips off the whitespace on the right side of the string
lstrip() method:strips off the whitespace on the left side of the string
strip() method: strips off the whitespace on both side(right and left) of the string
"""

string1 = 'Monty Python'

# for letter in string1:
#     print(letter)

# slicing from 0 up to 4 not including 4
print(string1[0:4])


# if second number is beyond the end of the string, it prints out from the first character to the last character
print(string1[6:20])


# the starting or ending number can be eliminated
# eliminating the ending number
print(string1[6:])

# eliminating the starting number
print(string1[:3])

# NOTE: using the " : "   prints out the whole string
print(string1[:])

# Using the " + " as an operator for string concantenation
print(string1 + " is very good")


# Using " in " as logical operator
if 'P' in string1:
    print("found")
else:
    print("Not found")


#Searcha and replace method:
string1.replace('Python', 'Javascript')
