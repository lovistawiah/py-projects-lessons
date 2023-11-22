"""
Strings are an ordered collection of characters used to store text and bytes based information

Strings are objects.
Strings can be iterated since is an array 
String object has  a lot of methods,
the string object is larger in memory
Python keeps both the stirng's length and text in memory
r: before strings enquoted are usually used to open files and regular expressions.
Concatenating number and a string result in an error
strings can be multiplied, concatenated.
String offset start at 0 and end at one less than the string length.
Negative offset are also useful. they begin at the end of length of the string.for example, -1 returns the last character of the string
"""
import sys

# INDEXING AND SLICING
s = 'spam'
# print upto not including the last character of the string
print(s[:-1])

# print from index 1 upto not including index 3
print(s[1:3])

# print the whole string
print(s[:])


# EXTENDED SLICING
# NOTE: variable declarartion using capital letter as beginning or capital letters are Constants
S = 'abcdefghijklmnop'
print(S)

# NOTE:slice opetator accepts more than two optional arguments. when three arguments are invoked, the first becomes the starting offset(default is zero(0) ), the secomd is the ending offset(one less than the length of the string or (-1) ), the third optional argument becomes the stepping offset(default is +1). the stepping offset is used to skip,reverse the order of the  items in the string
print(S[1:10:2])

# print everything stepping by 2
print(S[::2])

# reversing the order of the string using negative integer as the stride or the stepping offset
print('hello'[::-1])


# CHARACTER CODE CONVERSION

# ord(): the built-in function converts a  single character to its underlying integer code (ASCII byte value).
# chr(): this built-in function does the opposite of the ord() function
case = ''
case2 = ''
integerCode = ord('a')
print(integerCode)
print(chr(integerCode-32))
for c in 'hello':
    # NOTE: using the built-in function ord(),chr() and  -32 integer to make uppercase of a string
    case = case + chr(ord(c)-32)

print(case)

for c in 'LOVIS':
    # NOTE: using the built-in function ord(),chr() and  +32 integer to make lower case of a string
    case2 = case2 + chr(ord(c)+32)
print(case2)

# getting the ascii character set using the ord() and chr() built-in functions
for i in range(33, 256, 1):
    char = chr(i)
    integer = ord(chr(i))
    print(f'{integer} ==> {char}')


# BINARY
# converting integer values to binary values
binary = (bin(346))
print(binary)

# converting binary values to integer values
integerValues = int(binary, 2)
print(integerValues)


# Strings
# they are immutable sequence.characters of the string cannot be modified.
# NOTE: modification can be done, by assigning, building, indexing, slicing, and concatenating to its orginal string variable

S = 'spam'
print(S)

S = S + 'SPAM!'  # modifing by concatenating new values to existing values
print(S)

# the replace method can be used to achieve similar result
S = S.replace('pam', 'plot')
print(S)

#DICTIONARY-BASED Conversion

dictConversion = '%(qty)d more %(food)s' %{'qty':1, 'food':'spam' }
print(dictConversion)

#NOTE: dictionaary keys accessed using square brackets and dot( . ) for object attributes
dictConversion1 ='My {1[kind]} runs {0.platform}'.format(sys,{'kind':'laptop'})
print(dictConversion1)


