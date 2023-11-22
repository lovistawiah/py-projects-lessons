# ways of creating tuples

# comma separated objects
T = 0, 4, 6
# using tuple constructor
t = tuple('lovis')
# empty tuple
tu = ()

# tuples support a lot of operations

# concatenation,repetition
print(T+t)
print(t*3)


# NOTE: To make a single tuple expression use comma at the end of the object in the parenthenses
single = (40,)
single1 = (40)
print(f'single is a {type(single)} and single1 is a {type(single1)}')
# does membership test
for i in t:
    print(i)
print(T)
