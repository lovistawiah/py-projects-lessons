import sys
a = 3
print(type(a))

print(isinstance(4, int))
# NOTE: an entire list can be copied using the slice notation

L1 = [3, 4, 6, 3]
# copying an entire list using slice notation
l2 = L1[:]
print(l2)

# dictionary cannot be copied using the slicing notation, dictionaries are not sequenced
# NOTE: the appropriate way to copy an entire dict is to use the copy method

# ==: checks for equality: referencing the same object values
# is: checks for object identity


print(sys.getrefcount(a))
