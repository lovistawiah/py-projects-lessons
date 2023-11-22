# Programs are composed of modules
# Modules contain statements
# Statement contain expressions
# Expressions create and process objects

# ?         NUMBERS

# integers- numbers that have no fractional point,
# floating point numbers- have fractional point
# complex numbers- have imaginary parts
# decimals- with fixed precision
# rational numbers- with numerator and denominator


# ?          STRINGS
# strings are used to record both textual information as well as arbitrary collection of bytes
# strings are sequences of one-character strings

# ?          SEQUENCE OPERATIONS
S = 'spam'
print(S)
first_sequence = S[0]  # the first item in S, indexing by zero-based position
print(first_sequence)
last_sequence = S[-1]  # the last item from the end in S
print(last_sequence)

#        slicing
slicing = S[1:3]  # slice of S from offsets 1 through 2 (not 3)
print(slicing)

# NOTE: in a slice, the left bound defaults to zero, and the right bound defaults to the length of the sequence being sliced. Eg
slicing = S[1:]  # everything excluding the first item (1:len(S)) 'pam'
print(slicing)

slicing = S[0:3]  # everything excluding the last

slicing = S[:]  # copying an entire string
print(slicing)
con = S + 'xyz'  # concatenation of two strings
print(con)

print(S)  # Unchanged
rep = S*8  # repetition
print(rep)


# NOTE: strings are immutable, you can never overwrite the values of immutable objects.
# You can't change a string by assigning to one of its positions
# Example:
# S[0] = 'r'  # will result typeError: 'str' object does not support item assignment
print(S)


# NOTE: every Python object is immutable or not

# How to change character(s) in text-based data

S = 'Lovis'  # assignment
L = list(S)  # make it a list of char(s)
print(L)
L[2] = 'c'  # change in place using assignment
print(L)
print('before:', S)
S = ''.join(L)  # join  item using empty delimiter and join method
print('after:', S)

# ? Type-Specific method
S = 'Spam'
S.find('pa')  # find the offset of a substring in S
S.replace('pa', 'pu')  # replace old substring with new substring

line = 'aaa,bbb,ccc'
line.split(',')  # split on delimiter into a list of substrings
line = 'aaa,bbb,ccc\n'
print(line.rstrip()) #rstrip() removes whitespace characters on the right side

#NOTE: strings methods can be chained
#Example:
line.rstrip().split(',')


#?    FORMATTING STRINGS
s = '%s, eggs, and %s' %('spam', 'SPAM!') #formatting expression
print(s)

s= '{0},{1}'.format('spam','SPAM') #using format method
print(s)

s= '{},{}'.format('spam','SPAM') #using format method with numbers optional
print(s)

num = '{:,.3f}'.format(296999.2567) #using delimiters(, _) as separators and decimal digits
print(num)

num ='%.2f | %+05d ' %(3.14159, -42)
print(num)

#? GETTING HELP
# using dir()
print(dir(S))
print('hello')
print(dir([]))
print('hello')
print(dir({}))

# ? using help() 
# print(help(str))

# other ways to code Strings
print(ord('\n')) # returns unicode for one character

#?  LIST

#list- are positionally ordered collections of arbitrary typed objects, and they have no fixed size
#list is also mutable(changeable), list can be modified in place by assignment to offsets as well as variety of method calls. NOTE: known as array in JavaScript.


#Sequence Operations
Li = [123,'spam',1.23]
len(Li) #getting the length or number of items in the list

#we can index, slice and so on, just as for strings
Li[0] #indexing by position

Li[:-1] #NOTE: slicing a list returns a new list

Li + [34,32,1] #concatenation makes a new list

Li*2 #repetition also make a new list

print(Li) #returning the original list 

# Type-Specific Operations
# NOTE: Python's List has not fixed type constraint,they contain any type.
# They can grow and shrink on demand, in response to list-specific operations

Li.append('ni') #adding object to end of the list

Li.pop(2) #shrinking by removing or deleting an item by indexing.

#Bounds Checking
#NOTE: Although lists have no fixed size, Python does not allow us to reference items that are  not present. Indexing off or assigning off the end of the list is always a mistake 
#It will always result IndexError: list index out of range OR list assignment index out of range.

#Example:
Li[99] =1 # will result in IndexError: list assignment index out of range


