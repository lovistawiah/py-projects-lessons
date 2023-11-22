"""
tuples are similar to list.
they are immutable: they cannot be modified when created
tuples use parenthesis not square braces
tuples does destructuring assigment eg: (var1,var2....varN) =(value1,value2.....valueN) each variable should have a value on the right side.It also assign values(right side) to variables(left side) respectively
"""
di = {
    'a': 20,
    'b': 13,
    'c': 87,
    'd': 90,
    'e': 79
}

temp = list()
for k, v in di.items():
    temp.append((v, k))

temp = sorted(temp, reverse=True)
print(temp)
