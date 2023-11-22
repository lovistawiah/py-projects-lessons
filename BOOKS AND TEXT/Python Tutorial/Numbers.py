# A complete inventory of Python's numeric toolbox includes:
# 1. Integer and floating points objects
# 2. Complex number objects
# 3. Decimal: fixed precision objects
# 4. Fraction: rational numbers objects
# 5. Sets: collection with numeric operations
# 6. Booleans: true and false
# 7. Built-in function and modules: round,math,random, etc
# 8. Expression: unlimited integer precision, bitwise operations, hex, octal, and binary formats
# 9. Third party extension: vectors, libraries, vizualization, plotting etc


# INTEGERS AND FLOATING POINT LITERALS:
# integers are written as strings of decimal digits. floating-point numbers have a decimal point and/or an optional signed exponent introduced by e or E and followed by an optional sign


# HEXADECIMALS,OCTAL,BINARY:
# Integers can be coded in decimal(base 10), hexadecimal(basse16), octal(base 8), binary(base 2). Hexadecimals start with ox or OX followed by a string hexadecimal digits(0-9 and A-F). Octal numbers start with 0o or 00(leading zero and lower of upper case letter o), followed by a string of digits(0-7).Binary literals with ob or OB, followed by zero and/or one (0-1) called binary digits

# COMPLEX NUMBERS:
# Python complex literals are written as realPart + imaginaryPart, where the imaginary part is terminated with j or J. The real Part is technically optional, so the imaginary part may appear on its own. Complex numbers can be created using the complex(real,imag) built-in call. They are pairs of floating-point numbers

# NOTE:polymorphism—a term
# indicating that the meaning of an operation depends on the type of the objects being
# operated on.

#   Set is an unordered collection  of unique  and an immutable objects. The set itself is an object
#Set contain immutable objects and therefore list and dictionaries can not be embedded
x = set('abcde')
y = set('wxyz')

print(x | y) #union
print(x - y) #difference
print(x & y) #intersection
print(x ^ y) # symmetric difference


print(dir(y))

#BOOLEANS
#primitively, true and false are 1 and 0 respectively, they are also treated as integers therefore can be added as numbers
print(True + 4)
