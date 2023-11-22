yes_votes =45_670_900
no_votes =42_000_009
percentage = yes_votes /(yes_votes + no_votes)
print(percentage)
#format() method: accepts arguments(variables) that are used to replace placeholders in a string typically in square braces.
#NOTE:the replacement is done in first placeholder first variable
print('{:-9} YES VOTES {:2.2%}'.format(yes_votes,percentage))

#str(): this function return the represention of values that are human-readable

s ='Hello world'
print(str(s))

#repr() this function genetates the represention that can be read by the intepreter
print(repr(s))

print(str(1/7))
x = 200 *3.24
y =200 *300
s ='the value of x is '+repr(x)+' and the value of y is '+ repr(y) +'.....'
print(s)
import math
f = f'the round of pi is approximately {math.pi:.3f}'
print(f)

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}

for name,phone in table.items():
    #NOTE: using " : " and an integer after a variable in f-string expression creates wide column apart from the variable when printed 
    print(f'{name:10}==>{phone:10d}')

#NOTE: Other modifiers can be used to convert the value before it is formatted. '!a' applies ascii()==quote the string with single quotes, '!s' applies str(), and '!r' applies repr()==quote the string with single quotes:

animals = 'eels'

print(f'My favourite animals are:{animals!r} ===repr()')
print(f'My favourite animals are:{animals!a} ===ascii()')
print(f'My favourite animals are:{animals!s} ===str()')
print(f'My favourite animals are:{animals}')

#the string format method
#the basic use of string format is to replace square braces with the argument in the method in ascending order 

print('My name is {} {}'.format('Lovis','Tawiah'))

#The brackets and characters within them (called format fields) are replaced with the objects passed into the str.format() method. A number in the brackets can be used to refer to the position of the object passed into the str.format() method.
print('Lovis loves {0} and She loves {1}'.format('Sandra','Lovis'))
print('{1} are {0}'.format('red','Roses'))

#NOTE: if keyword are used in the square braces,the keyword must be assigned to a value to replace it like variable declaration

print('I attend {highSchool} and college at {College}'.format(highSchool ='UPSHS',College='IPMC'))

#Positional and keyword arguments can be arbitrarily combined

print('the story of {0}, {1} and {other}'.format('Lovis','Sandra',other='UPSHS'))


table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}


#If you have a really long format string that you don’t want to split up, it would be nice if you could reference the variables to be formatted by name instead of by position. This can be done by simply passing the dict and using square brackets '[]' to access the keys
print('Sjoerd: {0[Sjoerd]:d}; Jack: {0[Jack]:d}, Dcab: {0[Dcab]:d}'.format(table))

#This could also be done by passing the table as keyword arguments with the '**' notation.
print('Jack: {Jack:d}, Sjoerd: {Sjoerd:d}, Dcab: {Dcab:d}'.format(**table))

for x in range(1,11):
    print('{0:2d} {1:3d} {2:4d}'.format(x,x*x,x*x*x))

#Manually Formatting Strings
for x in range(1,11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    #NOTE: the use of 'end ' on the previous line
    print(repr(x*x*x).rjust(4))

print('-3.14'.zfill(5))


#old string formatting 
print('the value of pi is approximately %.3f'%math.pi)